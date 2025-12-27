from huggingface_hub import InferenceClient
import os

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=os.getenv("HF_TOKEN")
)

print(client.text_generation("Say OK in one word."))
