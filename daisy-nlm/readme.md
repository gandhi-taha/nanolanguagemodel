# Daisy NLM 🌼

**Hey there!** Welcome to `daisy-nlm` - your new best friend for running AI models right on your computer. No cloud services, no API keys to remember, no data leaving your machine. Just pure, simple AI that works.

Think of this as AI for the rest of us. You don't need a PhD or a server farm. Just install it and start chatting with AI models in seconds.

---

## Table of Contents

1. [Why You'll Love This](#why-youll-love-this)
2. [Quick Start](#quick-start-seriously-its-quick)
3. [Installation & Setup](#installation--setup)
4. [The Models](#the-models-the-cool-stuff)
5. [What Can You Do?](#real-talk-what-can-you-actually-do)
6. [Model Architecture](#model-architecture-deep-dive)
7. [Configuration](#configuration-and-customization)
8. [Advanced Features](#advanced-features)
9. [External APIs](#external-api-integration)
10. [Custom Models](#custom-model-integration)
11. [Examples](#build-something-fun)
12. [Performance](#performance-stuff)
13. [Troubleshooting](#troubleshooting)
14. [Contributing](#contributing)

---

## Why You'll Love This

- **Privacy First**: Everything runs on YOUR computer. Your data never leaves your machine.
- **Stupidly Simple**: Three functions. That's it. `do()`, `complete()`, and `chat()`.
- **Actually Fast**: Powered by IBM's Granite 3.0 and other efficient models
- **Works Offline**: After first download, internet? Who needs it.
- **Tiny Footprint**: Starts at just 512MB RAM. Works on a potato 🥔

## Quick Start (Seriously, It's Quick)

```bash
pip install daisy-nlm
```

```python
import daisynlm as nlm

# That's it. You're done. Now talk to AI:
nlm.do("What's the meaning of life?")
# Output: "The meaning of life is subjective and varies for each person..."

nlm.do("Translate to French: I love pizza")
# Output: "J'adore la pizza"

nlm.complete("The best thing about coding is")
# Output: "solving problems and creating something from nothing"
```

**First run?** Yeah, it'll download a model (~3GB for Granite). Grab a coffee ☕. After that? Lightning fast ⚡.

## The Models (The Cool Stuff)

### IBM Granite 3.0 (Our Favorite)

We're using **IBM Granite 3.0 3B-A800M** as the default. Why? Because it's awesome:

- **3 billion parameters** of smartness
- **MoE (Mixture of Experts)** architecture - fancy words for "really efficient"
- Built by IBM for enterprise quality
- Apache 2.0 license - use it however you want
- Great at reasoning, coding, and conversation

But don't worry, we've got others too if you want something lighter or heavier.

## Real Talk: What Can You Actually Do?

### Have a Conversation

```python
import daisynlm as nlm

nlm.chat("Hey! What's your favorite programming language?")
# Output: "I appreciate Python for its readability..."

nlm.chat("Can you help me debug some code?")
# Output: "Of course! Please share the code..."
```

### Get Answers

```python
import daisynlm as nlm

nlm.do("Explain quantum computing like I'm 5")
# Gets you a simple explanation

nlm.do("What's the capital of Japan?")
# Output: "Tokyo"
```

### Translate Stuff

```python
import daisynlm as nlm

nlm.do("Translate to Spanish: Where is the library?")
# Output: "¿Dónde está la biblioteca?"
```

### Make Decisions

```python
import daisynlm as nlm

sentiment = nlm.do(
    "Is this positive or negative: This movie was terrible!",
    choices=["positive", "negative"]
)
# Output: "negative"
```

### Finish Your Sentences

```python
import daisynlm as nlm

nlm.complete("My favorite thing about AI is")
# Output: "how it can augment human creativity and productivity"
```

## Customize It Your Way

### Want a Bigger Brain?

```python
import daisynlm as nlm

# Use more RAM for smarter models
nlm.config["max_ram"] = "8gb"  # Options: 0.5, 1, 2, 4, 8

# Now you're running with the big boys
nlm.do("Explain the theory of relativity")
```

### Got a GPU?

```python
import daisynlm as nlm

# Let's use that gaming rig for something useful
nlm.config["device"] = "auto"  # Automatically uses GPU if available

# Now everything runs WAY faster
```

### Available Models (Pick Your Fighter)

| RAM Need | Model | Size | Vibe |
|----------|-------|------|------|
| 512MB | LaMini-Flan-T5-248M | 248M | Quick & Dirty |
| 1GB | LaMini-Flan-T5-783M | 783M | Pretty Good |
| 3GB | **IBM Granite 3.0** | 3B | The Sweet Spot ⭐ |
| 4GB | Flan-Alpaca-GPT4-XL | 3B | Also Great |
| 8GB | OpenChat-3.5 | 7B | Boss Mode |

The model auto-picks based on your RAM. But you can force one if you want:

```python
import daisynlm as nlm

# Check what you're using
print(nlm.config["instruct_model"])

# Set RAM limit
nlm.config["max_ram"] = "3gb"  # Perfect for Granite 3.0
```

## Cool Tricks

### Search Your Documents

```python
import daisynlm as nlm

# Store some knowledge
nlm.store_doc("Python was created by Guido van Rossum in 1991", "python_info")
nlm.store_doc("JavaScript runs in the browser", "js_info")

# Ask questions about it
context = nlm.get_doc_context("Who made Python?")
nlm.do(f"Answer: {context}")
# Output mentions Guido van Rossum
```

### Pull from Wikipedia

```python
import daisynlm as nlm

# Get info from Wikipedia
wiki_text = nlm.get_wiki("Artificial Intelligence")
summary = nlm.do(f"Summarize this in 2 sentences: {wiki_text[:500]}")
```

### What Time Is It?

```python
import daisynlm as nlm

# Get current date/time
now = nlm.get_date()
print(now)  # "Monday, November 18, 2025 at 03:45PM"
```

## Build Something Fun

### Simple Chatbot

```python
import daisynlm as nlm

print("🤖 Chatbot ready! Type 'bye' to exit\n")

conversation = ""

while True:
    user = input("You: ")
    if user.lower() in ['bye', 'exit', 'quit']:
        print("👋 See you later!")
        break
    
    conversation += f"User: {user}\nAssistant: "
    response = nlm.chat(conversation)
    conversation += f"{response}\n"
    
    print(f"🤖: {response}\n")
```

### Translation Tool

```python
import daisynlm as nlm

def translate(text, language):
    return nlm.do(f"Translate to {language}: {text}")

print(translate("Hello, how are you?", "Spanish"))
print(translate("Hello, how are you?", "French"))
print(translate("Hello, how are you?", "Japanese"))
```

## IBM Granite 3.0: The Details

Since we're using Granite as our star model, here's what makes it special:

- **Mixture of Experts (MoE)**: Only activates the parts it needs. Saves memory, runs fast.
- **3B parameters total, 800M active**: Big brain, small footprint
- **Trained on diverse data**: Code, conversations, reasoning tasks
- **Apache 2.0**: Free for everything, including commercial use
- **Efficient**: Runs great on CPUs, amazing on GPUs

To use it specifically:

```python
import daisynlm as nlm

# Make sure you have 3GB+ RAM available
nlm.config["max_ram"] = "3gb"
nlm.config["instruct_model"] = "granite-3.0-3b-a800m-instruct"

# Now you're running Granite!
nlm.do("Explain the difference between AI and ML")
```

## Performance Stuff

We use some smart tricks to make things fast:

- **int8 quantization**: Makes models 4x smaller with minimal quality loss
- **CTranslate2 backend**: 2x faster than standard HuggingFace
- **Smart caching**: Downloads once, uses forever

Real numbers on a normal laptop (CPU):
- **Loading**: ~2 seconds
- **Simple query**: ~1-2 seconds
- **Long response**: ~5-10 seconds

With GPU? Cut those times in half or more.

## Where Models Live

First time you run, models download to:
```
~/.cache/huggingface/hub/
```

You can check what's there:
```python
import os
cache = os.path.expanduser("~/.cache/huggingface/hub")
print(f"Your models are in: {cache}")
```

## Privacy Matters

Let's be real clear about this:

✅ **Local by default**: All inference happens on YOUR machine  
✅ **No telemetry**: We don't track anything  
✅ **No cloud calls**: Unless you explicitly add API keys  
✅ **Offline capable**: Works without internet after first download  
✅ **Your data stays yours**: Always

## External APIs (If You Want Them)

Want to use OpenAI or other services sometimes? Cool:

```python
import os

# Add your OpenAI key
os.environ["DAISYNLM_OA_KEY"] = "sk-your-key-here"

import daisynlm as nlm

# Now it routes to OpenAI when beneficial
nlm.do("Complex task needing GPT-4")
```

But honestly? The local models are usually good enough.

## Examples You Can Run

Check out the `examples/` folder:

- **`chat.py`**: Terminal chatbot
- **`streamlitchat.py`**: Web-based chat UI  
- **`assistant.py`**: Document-aware assistant
- **`translate.ipynb`**: Translation notebook

Run them like:
```bash
python examples/chat.py

# Or for the web version:
pip install streamlit
streamlit run examples/streamlitchat.py
```

## Troubleshooting

**"It's slow!"**
```python
nlm.config["max_ram"] = 0.5  # Use smaller model
# or
nlm.config["device"] = "auto"  # Use GPU
```

**"Out of memory!"**
```python
nlm.config["max_ram"] = 0.5
nlm.config["max_tokens"] = 50  # Shorter responses
```

**"Models won't download!"**
- Check your internet
- Check disk space (need ~5GB)
- Try: `pip install --upgrade huggingface_hub`

**"Import error!"**
```bash
pip uninstall daisy-nlm
pip install daisy-nlm
```

## Requirements

- **Python**: 3.8 or newer
- **RAM**: 512MB minimum (3GB recommended for Granite)
- **Storage**: ~5GB for model cache
- **OS**: Windows, Mac, or Linux
- **GPU**: Optional but nice (NVIDIA with CUDA)

## Contributing

This is a learning-friendly project. Want to add something cool? Go for it! The code is pretty straightforward.

## License

MIT License - Do whatever you want with it.

The models have their own licenses:
- IBM Granite 3.0: Apache 2.0 (use freely!)
- Others vary - check the model info for details

## Credits

Built with love on top of:
- HuggingFace for model hosting
- CTranslate2 for fast inference
- IBM for the amazing Granite models
- Original languagemodels project (we evolved from there)

## Questions?

Read the docs in this repo:
- **`QUICKSTART.md`**: Get started in 5 minutes
- **`MODEL_CONNECTION_GUIDE.md`**: Deep dive into how it works
- **`INSTALLATION.md`**: Detailed setup instructions

## Final Words

AI doesn't have to be complicated. It doesn't have to live in the cloud. And it definitely doesn't have to cost money or sell your data.

This is AI for everyone. Simple, private, and powerful.

Now go build something cool! 🚀

```python
import daisynlm as nlm
nlm.do("What should I build first?")
```

---

## Installation & Setup

### Prerequisites

- **RAM**: Minimum 512MB (3GB+ recommended for Granite)
- **Internet**: Required for first-time model download
- **Optional**: NVIDIA GPU with CUDA for acceleration

### Installation Methods

We support two main ways to install: via Conda or using your System Python.

#### Option 1: Conda (Recommended)

If you use Anaconda or Miniconda:

```bash
conda create -n daisy-env python=3.11
conda activate daisy-env
pip install daisy-nlm
```

#### Option 2: System Python

Install directly to your system python (no Homebrew required):

```bash
# Install directly
pip3 install daisy-nlm
```

*Note: We do not recommend using Homebrew python for this package.*

### Verify Installation

```python
import daisynlm as nlm

# Check version
print(nlm.__version__)

# Test basic functionality
response = nlm.do("Say hello")
print(response)
```

### First Run

On first use, the library will:

1. Download the default model (~3GB for Granite) from Hugging Face
2. Cache it in `~/.cache/huggingface/hub/` (or your custom `cache_dir`)
3. Load and initialize the model

This takes 1-5 minutes depending on your connection. Subsequent runs are instant.

```python
import daisynlm as nlm

# This triggers the download on first run
nlm.do("Hello world")
```

# Install package
pip install daisy-nlm

# When done, deactivate
deactivate
```

### Platform-Specific Notes

**macOS**: Works on both Intel and Apple Silicon (M1/M2/M3)
```bash
pip install daisy-nlm
```

**Linux**: May require additional dependencies
```bash
# Ubuntu/Debian
sudo apt-get install python3-dev
pip install daisy-nlm
```

**Windows**: Install through PowerShell or Command Prompt
```powershell
pip install daisy-nlm
```

### Environment Variables (Optional)

For external APIs:

```bash
# OpenAI
export DAISYNLM_OA_KEY="your-openai-api-key"

# TextSynth
export DAISYNLM_TS_KEY="your-textsynth-key"
export DAISYNLM_TS_SERVER="https://api.textsynth.com"
```

---

## Model Architecture Deep Dive

### Understanding Model Types

The library supports three types of models:

#### 1. **Instruct Models** (Default)
- **Purpose**: Following instructions, Q&A, general tasks
- **Examples**: IBM Granite 3.0, LaMini-Flan-T5, OpenChat, Llama-3
- **Usage**: `nlm.do()`, `nlm.chat()`

```python
import daisynlm as nlm

# Uses instruct model
nlm.do("Translate to French: Hello world")
nlm.chat("Tell me about machine learning")
```

#### 2. **Completion Models**
- **Purpose**: Text continuation, code completion
- **Examples**: CodeT5+, GPT-style models
- **Usage**: `nlm.complete()`

```python
import daisynlm as nlm

# Uses completion model
nlm.complete("The quick brown fox")
# Output: "jumped over the lazy dog"
```

#### 3. **Embedding Models**
- **Purpose**: Semantic search, document retrieval
- **Examples**: Sentence transformers
- **Usage**: `nlm.store_doc()`, `nlm.get_doc_context()`

```python
import daisynlm as nlm

# Uses embedding model
nlm.store_doc("Python is a programming language", "doc1")
context = nlm.get_doc_context("What is Python?")
```

### Model Selection Algorithm

Models are automatically selected based on:

1. **Available RAM** (`max_ram` config)
2. **Model fitness** (parameters must fit in RAM)
3. **Model priority** (newer/better models ranked higher)
4. **License requirements** (if filtering is enabled)

```python
import daisynlm as nlm

# View available models
from daisynlm.config import models

print("Available Instruct Models:")
for m in models:
    if m['tuning'] == 'instruct':
        size_gb = m['params'] * 8 / 8 / 1e9  # Approximate size
        print(f"  {m['name']}: {m['params']/1e9:.1f}B params, ~{size_gb:.2f}GB")
```

### How Local Models Work

`daisy-nlm` automatically downloads and manages models from Hugging Face Hub. Models are:

1. **Downloaded** from Hugging Face on first use
2. **Cached** locally in `~/.cache/huggingface/hub/`
3. **Quantized** using int8 for efficient inference
4. **Loaded** via CTranslate2 backend for fast CPU inference

### Checking Current Model

```python
import daisynlm as nlm

# See which model is currently active
print(f"Current model: {nlm.config['instruct_model']}")
print(f"Max RAM: {nlm.config['max_ram']} GB")

# Get detailed model information
from daisynlm.models import get_model_info
info = get_model_info("instruct")
print(f"Model name: {info['name']}")
print(f"Parameters: {info['params']/1e9:.1f}B")
print(f"Size on disk: {info['size_gb']:.2f} GB")
print(f"Architecture: {info['architecture']}")
print(f"License: {info['license']}")
```

---

## Configuration and Customization

### Memory Configuration

Control which models can be used by adjusting RAM limits:

```python
import daisynlm as nlm

# Check current limit
print(f"Current max_ram: {nlm.config['max_ram']}")

# Set to 512MB (smallest models only)
nlm.config["max_ram"] = 0.5

# Set to 2GB (medium-quality models)
nlm.config["max_ram"] = "2gb"  # Can use string or float

# Set to 4GB (high-quality models)
nlm.config["max_ram"] = 4.0

# Set to 8GB (best available models)
nlm.config["max_ram"] = "8gb"

# After changing max_ram, check which model was selected
print(f"Selected model: {nlm.config['instruct_model']}")
```

### Device Configuration

Choose between CPU and GPU inference:

```python
import daisynlm as nlm

# Use CPU (default)
nlm.config["device"] = "cpu"

# Auto-detect and use GPU if available
nlm.config["device"] = "auto"

# Force GPU usage
nlm.config["device"] = "cuda"

# Check current device
print(f"Using device: {nlm.config['device']}")
```

### Inference Parameters

Fine-tune generation behavior:

```python
import daisynlm as nlm

# Maximum output length
nlm.config["max_tokens"] = 200  # Default: 200

# Prompt truncation limit
nlm.config["max_prompt_length"] = 4096  # Default: 4096

# Temperature (for direct API calls)
# Higher = more creative, Lower = more focused
from daisynlm.inference import generate

responses = generate(
    ["Explain AI"],
    max_tokens=100,
    temperature=0.7,  # 0.0 to 1.0
    topk=40  # Top-k sampling
)
```

### Manual Model Selection

Override automatic selection and choose a specific model:

```python
import daisynlm as nlm

# List available model names
from daisynlm.config import models
instruct_models = [m['name'] for m in models if m['tuning'] == 'instruct']
print("Available models:", instruct_models)

# Manually set a model
nlm.config["instruct_model"] = "openchat-3.5-0106"
nlm.config["max_ram"] = 8  # Must have enough RAM

# Now this will use the selected model
response = nlm.do("Hello, world!")
```

### Configuration Summary

```python
import daisynlm as nlm

# See all current settings
print(f"Model: {nlm.config['instruct_model']}")
print(f"RAM Limit: {nlm.config['max_ram']} GB")
print(f"Device: {nlm.config['device']}")
print(f"Max Tokens: {nlm.config['max_tokens']}")
print(f"Max Prompt Length: {nlm.config['max_prompt_length']}")

# Change multiple settings
nlm.config["max_ram"] = 2.0        # Use 2GB models
nlm.config["max_tokens"] = 100     # Shorter responses
nlm.config["device"] = "cpu"       # Force CPU usage
```

---

## Advanced Features

### Document Search and Retrieval

Store documents for semantic search and retrieval:

```python
import daisynlm as nlm

# Store documents with IDs
nlm.store_doc("Python is a programming language created in 1991", "python_doc")
nlm.store_doc("JavaScript is used for web development", "js_doc")
nlm.store_doc("Rust is a systems programming language", "rust_doc")

# Ask questions about your documents
context = nlm.get_doc_context("What year was Python created?")
print(context)
# Output: Information from python_doc about 1991

# Use context in questions
answer = nlm.do(f"Using this context: {context}, answer: When was Python made?")
print(answer)
```

### Wikipedia Integration

Pull information directly from Wikipedia:

```python
import daisynlm as nlm

# Get Wikipedia article
wiki_text = nlm.get_wiki("Artificial Intelligence")

# Store it for later
nlm.store_doc(wiki_text, "ai_info")

# Ask questions about it
context = nlm.get_doc_context("What is AI?")
answer = nlm.do(f"Answer using this context: {context}")
```

### Date and Time

Get current date and time in a readable format:

```python
import daisynlm as nlm

# Get current date/time
now = nlm.get_date()
print(now)  # "Monday, November 18, 2025 at 03:45PM"

# Use in prompts
response = nlm.chat(f"Current date: {now}. What day is it?")
```

### Weather Information

Get weather data (requires lat/lon coordinates):

```python
import daisynlm as nlm

# Get weather for location (Chicago coordinates)
lat, lon = 41.8781, -87.6298
weather = nlm.get_weather(lat, lon)

# Store and use it
nlm.store_doc(weather, "current_weather")
answer = nlm.do("What's the weather like?")
```

### Conversation Management

Build multi-turn conversations:

```python
import daisynlm as nlm

# Build conversation history
conversation = "System: You are a helpful assistant.\n\n"

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    
    # Add to conversation
    conversation += f"User: {user_input}\n\nAssistant: "
    
    # Get response
    response = nlm.chat(conversation)
    conversation += f"{response}\n\n"
    
    print(f"Assistant: {response}\n")
```

### Classification with Choices

Force the model to choose from specific options:

```python
import daisynlm as nlm

# Sentiment analysis
sentiment = nlm.do(
    "Classify sentiment: I love this product!",
    choices=["positive", "negative", "neutral"]
)
print(sentiment)  # Output: "positive"

# Topic classification
topic = nlm.do(
    "What topic is this? 'The stock market rose today'",
    choices=["sports", "finance", "technology", "politics"]
)
print(topic)  # Output: "finance"
```

---

## External API Integration

### OpenAI Integration

Connect to OpenAI's API when you need cloud-based models:

```python
import os
import daisynlm as nlm

# Set your OpenAI API key
os.environ["DAISYNLM_OA_KEY"] = "sk-your-api-key-here"

# Now regular calls will use OpenAI if configured
# The library detects the API key and routes requests accordingly
response = nlm.do("Explain quantum computing")
```

**Note**: Environment variable is `DAISYNLM_OA_KEY`

### TextSynth Integration

Connect to TextSynth API for alternative cloud inference:

```python
import os

# Configure TextSynth
os.environ["DAISYNLM_TS_KEY"] = "your-textsynth-api-key"
os.environ["DAISYNLM_TS_SERVER"] = "https://api.textsynth.com"  # Optional

# Use as normal
import daisynlm as nlm
response = nlm.do("What is the meaning of life?")
```

### Cloud vs Local Decision Flow

The library automatically decides between local and cloud:

```python
import daisynlm as nlm

# Priority order:
# 1. If DAISYNLM_OA_KEY is set → Use OpenAI
# 2. If DAISYNLM_TS_KEY is set → Use TextSynth
# 3. Otherwise → Use local model

# Force local even if API keys are set:
# (Remove API keys from environment)
import os
if "DAISYNLM_OA_KEY" in os.environ:
    del os.environ["DAISYNLM_OA_KEY"]
```

---

## Custom Model Integration

### Adding Custom Models from Hugging Face

You can integrate any compatible CTranslate2 model:

```python
import daisynlm as nlm
from daisynlm.config import models

# Add a custom model to the model list
custom_model = {
    "name": "my-custom-model",
    "tuning": "instruct",
    "params": 1.5e9,  # 1.5B parameters
    "quantization": "int8",
    "backend": "ct2",
    "architecture": "decoder-only-transformer",
    "license": "apache-2.0",
    "path": "username/model-name-ct2-int8"  # HuggingFace path
}

# Insert at the beginning (highest priority)
models.insert(0, custom_model)

# Set appropriate RAM limit
nlm.config["max_ram"] = 2.0

# The custom model may now be selected
print(f"Selected: {nlm.config['instruct_model']}")
```

### Using Local Model Files

If you have a pre-downloaded CTranslate2 model:

```python
import ctranslate2
from daisynlm.models import modelcache

# Load model from local path
local_model_path = "/path/to/your/ct2/model"
model = ctranslate2.Translator(
    local_model_path,
    device="cpu",
    compute_type="int8"
)

# Add to cache
modelcache["custom"] = (tokenizer, model)

# Now you can use it with the inference functions
```

### Model Format Requirements

For models to work with `daisy-nlm`:

1. **Format**: CTranslate2 format (not PyTorch/ONNX)
2. **Quantization**: int8 recommended for CPU
3. **Files needed**:
   - Model files (`model.bin`, `config.json`)
   - Tokenizer (`tokenizer.json`)
4. **Architecture**: One of:
   - `encoder-only-transformer` (BERT-style)
   - `decoder-only-transformer` (GPT-style)
   - `encoder-decoder-transformer` (T5-style)

---

## Troubleshooting

### Common Issues

#### Models are slow
```python
# Use smaller model
nlm.config["max_ram"] = 0.5

# Or enable GPU
nlm.config["device"] = "auto"
```

#### Out of memory
```python
# Reduce RAM limit
nlm.config["max_ram"] = 0.5

# Reduce output length
nlm.config["max_tokens"] = 50

# Truncate long prompts
nlm.config["max_prompt_length"] = 1024
```

#### Model won't download

```python
# Check internet connection
# Check HuggingFace Hub status: https://status.huggingface.co/

# Try manual download
from huggingface_hub import snapshot_download
from daisynlm.models import get_model_info

# Get the actual model path
info = get_model_info("instruct")
path = snapshot_download(
    info["path"],
    local_files_only=False
)
print(f"Downloaded to: {path}")
```

#### Model not found

```python
import daisynlm as nlm
from daisynlm.config import models

# List all available models
print("Available models:")
for m in models:
    print(f"  {m['name']} ({m['tuning']})")

# Make sure the model name matches exactly
nlm.config["instruct_model"] = "LaMini-Flan-T5-248M"  # Exact name
```

#### Import errors

```bash
# Reinstall package
pip uninstall daisy-nlm
pip install daisy-nlm

# Or upgrade dependencies
pip install --upgrade huggingface_hub ctranslate2
```

#### CTranslate2 errors

```bash
# Reinstall ctranslate2
pip uninstall ctranslate2
pip install ctranslate2>=4.4.0

# For GPU support
pip install ctranslate2[cuda]
```

### Cache Management

```python
import os
import shutil

# Find cache directory
cache_dir = os.path.expanduser("~/.cache/huggingface/hub")
print(f"Cache location: {cache_dir}")

# Check cache size
def get_dir_size(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += get_dir_size(entry.path)
    return total

if os.path.exists(cache_dir):
    size_gb = get_dir_size(cache_dir) / 1e9
    print(f"Cache size: {size_gb:.2f} GB")

# Clear cache (will re-download on next use)
# WARNING: This deletes all cached models
# shutil.rmtree(cache_dir)
```

### Debugging Model Loading

```python
import daisynlm as nlm

# Enable verbose output
import logging
logging.basicConfig(level=logging.DEBUG)

# Test model loading
from daisynlm.models import get_model, get_model_info

try:
    info = get_model_info("instruct")
    print(f"Model info: {info}")
    
    tokenizer, model = get_model("instruct")
    print(f"Model loaded successfully!")
    print(f"Model type: {type(model)}")
except Exception as e:
    print(f"Error loading model: {e}")
```

### Performance Monitoring

```python
import time
import daisynlm as nlm

# Benchmark inference speed
prompt = "What is artificial intelligence?"

# Warm-up (loads model into memory)
nlm.do("test")

# Time actual inference
start = time.perf_counter()
response = nlm.do(prompt)
elapsed = time.perf_counter() - start

print(f"Inference time: {elapsed:.2f}s")
print(f"Response length: {len(response)} chars")
print(f"Speed: {len(response)/elapsed:.1f} chars/sec")
```

### Offline Usage

After first download, the library works offline:

1. First run with internet: Downloads and caches model
2. Subsequent runs: Works without internet

To pre-download all models:

```python
import daisynlm as nlm

# Trigger downloads for different sizes
for ram in [0.5, 1.0, 2.0, 4.0]:
    nlm.config["max_ram"] = ram
    nlm.do("test")  # Downloads model if not cached
```

### Docker Installation (Advanced)

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

# Install dependencies
RUN pip install daisy-nlm

# Pre-download models (optional)
RUN python -c "import daisynlm as nlm; nlm.do('test')"

CMD ["python"]
```

Build and run:

```bash
docker build -t nlm-app .
docker run -it nlm-app
```

---

## Additional Resources

- **Hugging Face Hub**: https://huggingface.co/
- **CTranslate2 Documentation**: https://opennmt.net/CTranslate2/
- **Model Conversion Guide**: https://opennmt.net/CTranslate2/guides/transformers.html
- **IBM Granite Models**: https://huggingface.co/ibm-granite

---

## Quick Reference Card

```python
import daisynlm as nlm

# === BASIC USAGE ===
nlm.do("instruction")                    # Instruction following
nlm.complete("text to continue")         # Text completion
nlm.chat("message")                      # Chat/conversation

# === CONFIGURATION ===
nlm.config["max_ram"] = 4.0             # Set RAM limit (GB)
nlm.config["device"] = "auto"           # CPU/GPU selection
nlm.config["max_tokens"] = 200          # Max output length

# === MODEL INFO ===
print(nlm.config["instruct_model"])     # Current model name
from daisynlm.models import get_model_info
info = get_model_info("instruct")       # Detailed model info

# === EXTERNAL APIS ===
import os
os.environ["DAISYNLM_OA_KEY"] = "..."    # OpenAI
os.environ["DAISYNLM_TS_KEY"] = "..."    # TextSynth

# === DOCUMENT SEARCH ===
nlm.store_doc("content", "doc_id")      # Store document
nlm.get_doc_context("query")            # Retrieve context

# === UTILITIES ===
nlm.get_wiki("topic")                   # Get Wikipedia article
nlm.get_date()                          # Current date/time
nlm.get_weather(lat, lon)               # Weather data
```

---

## System Requirements Summary

### Minimum Requirements
- **CPU**: Any modern processor
- **RAM**: 512MB available
- **Storage**: 1GB free (for model cache)
- **OS**: Linux, macOS, or Windows
- **Python**: 3.8+

### Recommended Requirements
- **CPU**: Multi-core processor
- **RAM**: 4GB+ available
- **Storage**: 5GB free
- **GPU**: NVIDIA GPU with CUDA (optional)
- **Python**: 3.9+

---

## Dependencies

Automatically installed with the package:

- `huggingface_hub` - For downloading models
- `ctranslate2>=4.4.0` - Fast inference backend
- `tokenizers` - Text tokenization
- `numpy` - Numerical operations
- `sentence-transformers` - Embeddings

---

## Uninstallation

```bash
# Remove package
pip uninstall daisy-nlm

# Also clear cache if desired (optional)
rm -rf ~/.cache/huggingface/hub/
```

---

**Made with ❤️ for humans who just want AI at work**
