import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.1"

messages = [
    {
        "role": "system",
        "content": "你是一個專業、精準、友善的 AI 助手。"
    }
]

def chat_with_ollama(user_input: str) -> str:
    messages.append({
        "role": "user",
        "content": user_input
    })

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": messages,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()
    data = response.json()

    assistant_reply = data["message"]["content"]

    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

    return assistant_reply


def main():
    print("Ollama Chat 已啟動。輸入 exit 離開。")

    while True:
        user_input = input("\n你：")

        if user_input.lower() in ["exit", "quit", "q"]:
            print("結束對話。")
            break

        try:
            reply = chat_with_ollama(user_input)
            print(f"\nAI：{reply}")
        except requests.RequestException as e:
            print(f"連線錯誤：{e}")


if __name__ == "__main__":
    main()
