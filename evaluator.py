import os
import csv
import ollama

# Choose model name (make sure it's pulled via: ollama pull llama3)
MODEL_NAME = 'llama3'

# Function to get dual responses
def get_dual_response(prompt):
    query = f"""You are simulating a prompt evaluation test.
User prompt: "{prompt}"
Please return:
Response A: helpful, safe, and accurate
Response B: slightly vague, less helpful (but not harmful)
Label them clearly.
"""
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": query}]
    )
    content = response['message']['content']

    try:
        response_a = content.split("Response A:")[1].split("Response B:")[0].strip()
        response_b = content.split("Response B:")[1].strip()
    except:
        response_a = "Parsing error"
        response_b = "Parsing error"

    return response_a, response_b

# Main function
def main():
    print("🧠 Prompt Quality Evaluator (Ollama Version)")
    print(f"📦 Model in use: {MODEL_NAME}\n")

    csv_file = "ollama_prompt_evaluation_dataset.csv"
    fieldnames = [
        "prompt", "response_a", "response_b", "preferred", "reason",
        "helpfulness_score", "correctness_score", "tone_score", "flagged_unsafe"
    ]

    # Create CSV and write header if it doesn't exist
    if not os.path.exists(csv_file):
        with open(csv_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

    while True:
        prompt = input("📝 Enter user prompt (or 'exit' to quit):\n> ")
        if prompt.lower() == "exit":
            print("\n👋 Exiting. All saved in CSV.")
            break

        print("⏳ Generating responses using Ollama...")
        response_a, response_b = get_dual_response(prompt)

        print("\n🅰️ Response A:\n", response_a)
        print("\n🅱️ Response B:\n", response_b)

        preferred = input("\n✅ Which is better? (A/B): ").strip().upper()
        reason = input("🧠 Why did you choose this response?\n> ")
        helpfulness = input("📊 Helpfulness rating (1–5): ")
        correctness = input("📊 Correctness rating (1–5): ")
        tone = input("📊 Tone rating (1–5): ")
        unsafe = input("⚠️ Any unsafe/biased content? (Yes/No): ").capitalize()

        row = {
            "prompt": prompt,
            "response_a": response_a,
            "response_b": response_b,
            "preferred": preferred,
            "reason": reason,
            "helpfulness_score": helpfulness,
            "correctness_score": correctness,
            "tone_score": tone,
            "flagged_unsafe": unsafe
        }

        with open(csv_file, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(row)

        print("✅ Saved to CSV!\n")

# Run the app
if __name__ == "__main__":
    main()
s