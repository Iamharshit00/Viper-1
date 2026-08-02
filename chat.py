import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

# 1. Load Saved Model and Tokenizer
MODEL_ID = "distilgpt2"
OUTPUT_DIR = "./saved_llm_model"

print("Loading your saved AI...")
tokenizer = AutoTokenizer.from_pretrained(OUTPUT_DIR)
base_model = AutoModelForCausalLM.from_pretrained(MODEL_ID, torch_dtype=torch.float32)
model = PeftModel.from_pretrained(base_model, OUTPUT_DIR)
model.eval()

# 2. Chat Loop with Memory
chat_history = ""
chat_history_allowed = True  # Flag to allow or disallow chat history
print(
    "\nAI is ready to chat! Type 'exit' or 'quit' to end.\nType 'nohistory' to disable chat history for the next turn.\n"
  "--------------------------------------------------"
)

while True:
  user_input = input("You: ")
  if user_input.lower() in ["exit", "quit"]:
    print("Goodbye!")
    break
  elif user_input.lower() in ["nohistory"]:
    chat_history_allowed = False
    print("Chat history disabled. Starting fresh.")
    chat_history = ""
    continue

  # Append latest turn to chat history (Memory)
  if chat_history_allowed:
    chat_history += f"User: {user_input}\nAI:"
  else:
    chat_history = f" {user_input}\nAI:"

  # Tokenize input using the high-quality tokenizer
  inputs = tokenizer(chat_history, return_tensors="pt", truncation=True, max_length=512)

  # Generate response
  with torch.no_grad():
    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=100,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )

  # Decode output and extract only the new response
  full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)

  # Extract just the latest AI reply
  ai_response = full_response[len(tokenizer.decode(inputs["input_ids"][0], skip_special_tokens=True)):]
  ai_response = ai_response.split("User:")[0].strip() # Clean up trailing turns if any

  print(f"AI: {ai_response}")

  # Update history with the AI's response to keep context
  chat_history += f" {ai_response}\n"