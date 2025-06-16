from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from templates import construct_prompt
from postprocess import limit_text, remove_repetition, check_keywords_existence

def main():
    # 1. Load the model
    model_name = "aubmindlab/aragpt2-medium"
    print(f"Loading model: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
    print("Model loaded successfully.")

    # 2. User Input
    print("Please provide 3 Arabic keywords, separated by commas.")
    keywords_input = input("Enter keywords: ")
    keywords = [k.strip() for k in keywords_input.split(",")]

    if len(keywords) != 3:
        print("Error: Please provide exactly 3 keywords.")
        return

    # 3. Prompt Construction
    prompt = construct_prompt(keywords)
    print(f"\nConstructed Prompt: {prompt}")

    # 4. Text Generation
    print("\nGenerating text...")
    # You might need to adjust max_length and num_return_sequences based on desired output length
    # and model's capabilities.
    # Also, consider adding `pad_token_id` if the model's tokenizer requires it
    # (e.g., tokenizer.eos_token_id or tokenizer.pad_token_id)
    generated_texts = generator(prompt, max_length=150, num_return_sequences=1, do_sample=True)
    raw_generated_text = generated_texts[0]["generated_text"]
    print(f"Raw Generated Text: {raw_generated_text}")

    # Remove the prompt from the generated text
    if raw_generated_text.startswith(prompt):
        generated_text = raw_generated_text[len(prompt):].strip()
    else:
        generated_text = raw_generated_text.strip()

    # 5. Post-processing
    print("\nApplying post-processing...")
    processed_text = limit_text(generated_text)
    processed_text = remove_repetition(processed_text)
    
    found_keywords = check_keywords_existence(processed_text, keywords)

    # 6. Print the final result
    print("\n--- Final Output ---")
    print(processed_text)
    if found_keywords:
        print(f"Keywords found in output: {', '.join(found_keywords)}")
    else:
        print("No original keywords found in the output.")

if __name__ == "__main__":
    main() 