import requests
import os
import time

from config import ENDPOINT, HEADERS, MODELS


def generate_post(model_id: str, topic: str, style: str):
    prompt = (
        f"Write a detailed blog-style post about the topic '{topic}' in a '{style}' tone. "
        "Do not make anything up — mention only real facts or real companies if applicable. "
        "Make the writing catchy and engaging."
    )

    payload = {
        "model": model_id,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(ENDPOINT, headers=HEADERS, json=payload, timeout=60)

    if response.status_code == 200:
        data = response.json()
        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        elif "error" in data:
            return f"Error from model: {data['error'].get('message', 'Unknown error')}"
        else:
            return "Unexpected response format"
    else:
        return f"Error {response.status_code}: {response.text}"


def main():
    topic = input("Enter topic: ")
    style = input("Enter writing style (e.g., bold, expert, casual): ")
    print(f"Running prompt on {len(MODELS)} models...")

    os.makedirs("examples", exist_ok=True)

    for name, model_id in MODELS.items():
        print(f"→ Generating with {name}...")
        try:
            result = generate_post(model_id, topic, style)
            filename = f"examples/{name}_post.md"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"✔ Saved to {filename}")
            time.sleep(2)
        except Exception as e:
            print(f"❌ Failed for {name}: {str(e)}")


if __name__ == "__main__":
    main()
