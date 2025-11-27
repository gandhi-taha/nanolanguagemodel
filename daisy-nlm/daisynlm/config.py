"""
Global configuration for Daisy NLM.

This module handles the settings and model definitions. It ensures everything
is configured correctly so you don't have to worry about the details.
"""

import re
import os
from collections import namedtuple
from huggingface_hub import hf_hub_download
import json

ConfigItem = namedtuple("ConfigItem", "initfn default")


class ModelFilterException(Exception):
    pass


# List of available models.
# We sort these by priority - the best ones are at the top.
# The system picks the best model that fits in your RAM.
models = [
    {
        "name": "granite-3.0-3b-a800m-instruct",
        "repo": "t4gandhi/granite-3.0-3b-a800m-instruct-ct2-int8",
        "tuning": "instruct",
        "datasets": ["granite", "enterprise", "reasoning"],
        "params": 3e9,
        "quantization": "int8",
        "backend": "ct2",
        "architecture": "decoder-only-transformer",
        "license": "apache-2.0",
        "prompt_fmt": "<|user|>\n{instruction}\n<|assistant|>\n",
        "description": "IBM Granite 3.0 MoE model - 3B params total, 800M active. Great balance of quality and efficiency.",
    },
    {
        "name": "Qwen2.5-1.5B-Instruct",
        "repo": "t4gandhi/Qwen2.5-1.5B-Instruct-ct2-int8",
        "tuning": "instruct",
        "languages": [
            "zh",
            "en",
            "fr",
            "es",
            "pt",
            "de",
            "it",
            "ru",
            "ja",
            "ko",
            "vi",
            "th",
            "ar",
        ],
        "revision": "5de22ab",
        "datasets": [],
        "params": 1.5e9,
        "quantization": "int8",
        "backend": "ct2",
        "context_length": 32 * 1024,
        "repetition_penalty": 1.1,
        "architecture": "decoder-only-transformer",
        "license": "apache-2.0",
        "prompt_fmt": (
            "<|im_start|>system\nAnswer concisely.<|im_end|>\n"
            "<|im_start|>user\n{instruction}<|im_end|>\n"
            "<|im_start|>assistant\n"
        ),
    },
    {
        "name": "Mistral-7B-Instruct-v0.2",
        "repo": "t4gandhi/Mistral-7B-Instruct-v0.2-ct2-int8",
        "tuning": "instruct",
        "datasets": ["mistral"],
        "params": 7e9,
        "quantization": "int8",
        "backend": "ct2",
        "architecture": "decoder-only-transformer",
        "license": "apache-2.0",
        "prompt_fmt": "<s>[INST] {instruction} [/INST]",
    },
    {
        "name": "LaMini-Flan-T5-248M",
        "repo": "t4gandhi/LaMini-Flan-T5-248M-ct2-int8",
        "tuning": "instruct",
        "revision": "96cfe99",
        "datasets": ["c4", "flan", "lamini"],
        "params": 248e6,
        "quantization": "int8",
        "backend": "ct2",
        "architecture": "encoder-decoder-transformer",
        "license": "cc-by-nc-4.0",
    },
    {
        "name": "all-MiniLM-L6-v2",
        "repo": "t4gandhi/all-MiniLM-L6-v2-ct2-int8",
        "tuning": "embedding",
        "revision": "28efeb4",
        "params": 22e6,
        "quantization": "int8",
        "backend": "ct2",
        "architecture": "encoder-only-transformer",
        "license": "apache-2.0",
    },
]


class Config(dict):
    """
    Holds the configuration settings.
    It acts like a dictionary but checks that the values make sense.
    """

    model_names = {m["name"]: m for m in models}

    def __init__(self, config={}):
        # Start with default settings
        for key in Config.schema:
            self[key] = self.schema[key].default

        # Check environment variables (DAISYNLM_*)
        for key in Config.schema:
            value = os.environ.get(f"DAISYNLM_{key.upper()}")
            if value:
                self[key] = value

        # Apply any manual overrides
        for key in config.keys():
            self[key] = config[key]

    def __setitem__(self, key, value):
        super().__setitem__(key, Config.schema[key].initfn(value))

        # If memory or license settings change, re-evaluate the best model
        if key == "max_ram" or key == "model_license":
            found = set()
            for model in models:
                if model["quantization"] == "int8":
                    memsize = model["params"] / 1e9
                elif model["quantization"] == "q3_k_m":
                    memsize = model["params"] * 0.48 / 1e9
                elif model["quantization"] == "q4_k_m":
                    memsize = model["params"] * 0.59 / 1e9

                sizefit = memsize < self["max_ram"]

                if "model_license" in self:
                    licensematch = self["model_license"].match(model["license"])
                else:
                    licensematch = True

                if model["tuning"] not in found and sizefit and licensematch:
                    self[model["tuning"] + "_model"] = model["name"]
                    found.add(model["tuning"])

            if len(found) < 1:
                raise ModelFilterException("Unable to find models to match filters")

    def update(self, other):
        for key in other:
            self[key] = other[key]

    def use_hf_model(self, hf_path, revision, model_type="instruct"):
        """
        Load a model directly from Hugging Face.
        """

        assert "ct2" in hf_path.lower()
        assert "int8" in hf_path.lower()

        # Import jinja2 only when needed for chat templates
        from jinja2 import Environment, BaseLoader

        tok_config = hf_hub_download(
            hf_path, "tokenizer_config.json", revision=revision
        )

        with open(tok_config) as f:
            chat_template = json.load(f)["chat_template"]

        env = Environment(loader=BaseLoader())

        template = env.from_string(chat_template)

        prompt_fmt = template.render(
            messages=[{"role": "user", "content": "{instruction}"}],
            add_generation_prompt=True,
        )

        model = {
            "name": hf_path,
            "backend": "ct2",
            "quantization": "int8",
            "architecture": "decoder-only-transformer",
            "max_tokens": 2048,
            "params": 0,
            "prompt_fmt": prompt_fmt,
        }

        models.insert(0, model)
        self.model_names[model["name"]] = model
        self[f"{model_type}_model"] = model["name"]

    @staticmethod
    def validate_model(model_name):
        return Config.model_names[model_name]["name"]

    @staticmethod
    def validate_device(device):
        assert device in ["auto", "cpu"]

        return device

    @staticmethod
    def convert_to_gb(space):
        """
        Converts a memory string (like "4GB" or "512MB") into gigabytes (float).
        """

        if isinstance(space, int) or isinstance(space, float):
            return float(space)

        size_names = {
            "small": 0.2,
            "base": 0.48,
            "large": 1.0,
            "xl": 4.0,
            "xxl": 16.0,
        }

        if space.lower().strip() in size_names:
            return size_names[space.lower().strip()]

        multipliers = {
            "g": 1.0,
            "m": 2**-10,
        }

        space = space.lower()
        space = space.rstrip("b")

        if space[-1] in multipliers:
            return float(space[:-1]) * multipliers[space[-1]]
        else:
            return float(space)


Config.schema = {
    "max_ram": ConfigItem(Config.convert_to_gb, 0.48),
    "max_tokens": ConfigItem(int, 200),
    "echo": ConfigItem(int, False),
    "device": ConfigItem(Config.validate_device, "cpu"),
    "model_license": ConfigItem(re.compile, ".*"),
    "instruct_model": ConfigItem(Config.validate_model, "granite-3.0-3b-a800m-instruct"),
    "embedding_model": ConfigItem(Config.validate_model, "all-MiniLM-L6-v2"),
    "code_model": ConfigItem(Config.validate_model, "LaMini-Flan-T5-248M"),
    "max_prompt_length": ConfigItem(int, 50_000),
    "cache_dir": ConfigItem(str, os.path.join(os.getcwd(), "models")),
}

config = Config()

if "COLAB_GPU" in os.environ:
    if len(os.environ["COLAB_GPU"]) > 0:
        # Auto-enable GPU on Google Colab
        config["device"] = "auto"
