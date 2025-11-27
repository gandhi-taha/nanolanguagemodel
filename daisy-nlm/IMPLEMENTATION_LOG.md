# Nano Language Model 

**Project Goal**: Build a stupid-simple AI library that just works. 
**Status**: Core Complete | Training Debug Mode | Enhancement Phase

---

## My Implementation Story

### 1: The Vision - 
- [ ] Had enough of complex AI libraries
- [ ] Decided: "3 functions, that's it"
- [ ] Sketched out `do()`, `complete()`, `chat()`
- [ ] Set privacy-first goal (everything local)
- [ ] Picked IBM Granite 3.0 as default model

**Thoughts**: Keep it simple, stupid. If I can't explain it to my grandma, it's too complex.

---

### Config System - 
- [ ] Create `config.py` with global settings dict
- [ ] Add RAM constraints (0.5GB, 1GB, 2GB, 4GB, 8GB tiers)
- [ ] Device auto-detection (CPU/CUDA)
- [ ] Model registry with metadata
- [ ] Write `get_best_model()` selector logic

**Thoughts**: RAM-based selection is genius. Users don't need to know model names.

**Code Snapshot**:
```python
config = {
    "max_ram": 4.0,  # Start reasonable
    "device": "auto",  # Let me figure it out
    "max_tokens": 512,
    "temperature": 0.7
}
```

---

### Model Manager - 
- [ ] Set up `models.py` skeleton
- [ ] Integrate with Hugging Face Hub
- [ ] Implement download + cache logic
- [ ] Add transformers backend for inference
- [ ] Write `load_instruct_model()`
- [ ] Write `load_completion_model()`
- [ ] Write `load_embedding_model()`
- [ ] Test with tiny model first (LaMini-248M)
- [ ] Add 8-bit quantization option for memory efficiency

**Challenges**: 
- Initial attempt with CTranslate2 didn't work well on Windows/Linux
- Switched to pure transformers library - more compatible
- 8-bit loading helps a ton with memory
![CTranlate2](/media/image.png)
---

### Preprocessing Pipeline - 
- [ ] Create `preprocess.py`
- [ ] Research model prompt formats (pain in the ass)
- [ ] Implement Llama format: `[INST]...[/INST]`
- [ ] Implement Alpaca format: `### Instruction...`
- [ ] Implement ChatML format:
- [ ] Add Granite-specific formatting: 
- [ ] Write `format_instruction_prompt()`
- [ ] Write `format_chat_prompt()`
- [ ] Add output cleaning (strip special tokens)

**Notes**: Every model has its own special snowflake format. Why? God knows :D

---

### Inference Engine - 
- [ ] Build `inference.py` core
- [ ] Implement `generate_response()` with kwargs
- [ ] Add temperature/top_p/top_k sampling
- [ ] Implement constrained generation (choices list)
- [ ] Add `complete_text()` for completions
- [ ] Build `chat_completion()` with history
- [ ] Test with different prompt lengths
- [ ] Add max_tokens safety limit
- [ ] Profile inference speed (decent)

**Performance Notes**:
- Granite 3B: ~15-20 tokens/sec on decent CPU
- LaMini 248M: ~50-60 tokens/sec
- GPU makes it 10-15x faster depending on card
- 8-bit quantization: minimal quality loss, 50% memory savings


## The Magic - 

### Main API (`__init__.py`) - 
- [ ] Import everything cleanly
- [ ] Implement `do()` - the workhorse
- [ ] Implement `complete()` - text continuation
- [ ] Implement `chat()` - conversations
- [ ] Add docstrings (make them fun)
- [ ] Test all three functions end-to-end
- [ ] Add error handling (graceful failures)

**User Experience Goal**: "If you need more than 3 functions, I failed."

---

###  Document Store 
- [ ] Add embeddings support in `embeddings.py`
- [ ] Implement `store_doc()` function
- [ ] Implement `get_doc_context()` retrieval
- [ ] Use sentence-transformers for embeddings
- [ ] Add cosine similarity search
- [ ] Test with 100 documents
- [ ] Add persistence option (pickle)
- [ ] Write `store_doc()` and `get_doc_context()` in API

**Use Case**: "Let users build their own mini ChatGPT with their docs."

**Learning**: Embeddings are black magic but they work amazingly well.

---

## Documentation - 

### Write the Docs - DONE
- [ ] Create comprehensive `README.md`
- [ ] Write `QUICKSTART.md` (5-minute guide)
- [ ] Write `INSTALLATION.md` (all platforms)
- [ ] Write `MODEL_CONNECTION_GUIDE.md`
- [ ] Add examples folder with demos
- [ ] Create Jupyter notebooks (extractive QA, summarization)
- [ ] Proofread everything 3x

**Philosophy**: "If users need to ask questions, I didn't document it well enough."


## Current - Training Debug -

### LoRA Fine-tuning - 
- [ ] Set up PEFT/LoRA integration
- [ ] Load base Granite model
- [ ] Apply LoRA adapters
- [ ] Tokenize dataset
- [ ] Create training loop
- [ ] **FIX NaN LOSS** <- IMP
- [ ] Test with smaller learning rate
- [ ] Add gradient clipping
- [ ] Fix label masking (-100 for padding)
- [ ] Switch to float32 if needed
- [ ] Validate loss goes down
- [ ] Save fine-tuned adapter
- [ ] Test inference with adapter

**Debug Checklist**:
- [ ] Print model dtype (should be float32)
- [ ] Print first batch gradients
- [ ] Check if loss function is working
- [ ] Validate input_ids and labels shape
- [ ] Test with toy dataset (10 examples)
- [ ] Add gradient clipping (max_norm=1.0)
- [ ] Lower LR to 1e-6
- [ ] Check for inf/nan in inputs
- [ ] Verify tokenizer pad_token_id is correct
- [ ] Check if model is frozen (trainable params look right)

## Enhancement Backlog -

### External API Support -
- [ ] Add OpenAI API integration
- [ ] Add Anthropic Claude support
- [ ] Add TextSynth integration
- [ ] Allow seamless switching (same API)
- [ ] Document API key setup
- [ ] Test cost tracking

**Goal**: "Use local when possible, cloud when needed. Same interface."

---

### Custom Model Support -
- [ ] Document custom model format
- [ ] Add `register_model()` function
- [ ] Support local GGUF files
- [ ] Support local safetensors
- [ ] Test with custom fine-tuned model
- [ ] Write guide for adding models

---

### Performance Optimizations -
- [ ] Add 4-bit quantization (bitsandbytes)
- [ ] Implement KV cache for faster generation
- [ ] Add batch inference support
- [ ] Profile memory usage
- [ ] Optimize embedding search (FAISS?)
- [ ] Add streaming generation
- [ ] Benchmark against alternatives
- [ ] Test with different GPUs (3060, 4090, etc)

---

## Future Vision

**Where this could go**:
- [ ] Most downloaded local AI library
- [ ] Used in production apps
- [ ] Community contributes models
- [ ] Featured on Hugging Face
- [ ] 1000+ GitHub stars
- [ ] Used in AI education

**Personal Goal**: "Make AI accessible to everyone, not just for AI engineers."

---

## Known Issues

1. **Training NaN Loss**: Currently debugging loop.
2. **Memory Usage**: Large models can OOM on systems with <8GB RAM. Need better warnings.
3. **First Run Slow**: Model download takes time. Could add progress bars.
4. **GPU Detection**: Sometimes doesn't detect GPU correctly. Need better auto-detection.
5. **Token Limit**: Some models have hard limits. Need better handling of long inputs.