from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def generate_meal(prompt="Name:"):
    output = generator(prompt, max_length=150, num_return_sequences=1)
    return output[0]["generated_text"]
