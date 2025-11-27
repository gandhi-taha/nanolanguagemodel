import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

import daisynlm

print(f"Testing daisynlm v{daisynlm.__version__}")

# Force small model for testing speed
daisynlm.config["max_ram"] = 5
print(f"Using model: {daisynlm.config['instruct_model']}")

print("\n--- Testing daisynlm.do() ---")
try:
    response = daisynlm.do("Translate to Spanish: Hello friend")
    print(f"Input: Translate to Spanish: Hello friend")
    print(f"Output: {response}")
except Exception as e:
    print(f"FAILED: {e}")

print("\n--- Testing daisynlm.complete() ---")
try:
    prompt = "The quick brown fox"
    response = daisynlm.complete(prompt)
    print(f"Input: {prompt}")
    print(f"Output: {response}")
except Exception as e:
    print(f"FAILED: {e}")

print("\n--- Testing daisynlm.chat() ---")
try:
    chat_prompt = """
System: You are a helpful assistant.

User: What is the capital of France?

Assistant:
"""
    response = daisynlm.chat(chat_prompt)
    print(f"User: What is the capital of Germany?")
    print(f"Assistant: {response}")
except Exception as e:
    print(f"FAILED: {e}")

print("\n--- Testing RAG (store_doc / get_doc_context) ---")
try:
    daisynlm.store_doc("The secret code is 12345.", "secret_info")
    print("Stored document: 'The secret code is 12345.'")
    
    context = daisynlm.get_doc_context("What is the secret code?")
    print(f"Retrieved Context: {context}")
    
    answer = daisynlm.do(f"Based on this context: {context}, what is the secret code?")
    print(f"RAG Answer: {answer}")
except Exception as e:
    print(f"FAILED: {e}")

print("\n--- Tests Complete ---")
