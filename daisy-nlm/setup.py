import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="daisy-nlm",
    version="2.0.0",
    author="Taha Gandhi",
    author_email="tahagandhi551552@icloud.com",
    description="Your friendly Python companion for running mini AI models locally - zero hassle, maximum privacy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gandhi-taha/daisy-nlm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Natural Language :: English",
    ],
    python_requires='>=3.8',
    install_requires=[
        "huggingface_hub",
        "ctranslate2>=4.4.0",
        "tokenizers",
        "numpy",
        "requests",
       ],
)