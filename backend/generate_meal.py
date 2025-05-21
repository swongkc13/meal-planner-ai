from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

prompt = "Name:"
output = generator(prompt, max_length=150, num_return_sequences=1)

print("🍽️ Generated Meal:\n")
print(output[0]["generated_text"])
