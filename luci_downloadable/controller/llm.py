from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from huggingface_hub import InferenceApi

checkpoint = "bigcode/starcoder"
device = "cuda" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)


def llm_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
    outputs = model.generate(inputs)
    return tokenizer.decode(outputs[0])


# Example usage
if __name__ == "__main__":
    prompt = "Hi! Introduce yourself:"
    response = llm_response(prompt)
    print(f"Response from LLM:\n{response}")
