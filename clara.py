#!/usr/bin/env python3
import os
import requests
import readline
import time
from datetime import datetime

system_dir = os.path.expanduser("~/.clara")
env_file = os.path.join(system_dir, ".env")
logs_dir = os.path.join(system_dir, "logs")

with open(env_file) as f:
    for line in f:
        key, value = line.strip().split("=", 1)
        os.environ[key] = value

API_KEY = os.getenv("GEMINI_API_KEY")
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent"

history = []

os.makedirs(logs_dir, exist_ok=True)
timestamp = datetime.now().strftime("Clara_%Y%m%d_%H%M%S")
log_file = os.path.join(logs_dir, f"{timestamp}.md")

with open(log_file, "w") as f:
    f.write(f"# Clara {datetime.now().strftime('%Y/%m/%d %H:%M:%S')}\n")

print("💠 Clara - type 'exit' to quit.\n")

try:
    while True:
        entry = input("> ").strip()
        if entry.lower() == "exit":
            print("💠 Clara - view logs at '~/.clara/logs/'")
            break
        if not entry:
            print("💠 Huh?\n")
            continue
        history.append({"role": "user", "parts": [{"text": entry}]})
        for attempt in range(1):
            response = requests.post(
                URL,
                headers={"x-goog-api-key": API_KEY, "Content-Type": "application/json"},
                json={
                    "system_instruction": {
                        "parts": [
                            {
                                "text": "Your name is Clara, an AI assistant created by FJrodafo."
                            }
                        ]
                    },
                    "contents": history,
                },
            )
            data = response.json()
            if "candidates" in data:
                break
            print("💠 Sorry! I'm having trouble connecting. Retrying...")
            time.sleep(10)
        else:
            print("💠 Sorry! I'm unable to connect. Please try again...\n")
            history.pop()
            continue
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        history.append({"role": "model", "parts": [{"text": text}]})
        print(f"💠 {text}\n")
        with open(log_file, "a") as f:
            f.write(f"\n> {entry}\n")
            f.write(f"\n💠 {text}\n")
except KeyboardInterrupt:
    print("\n💠 Clara - view logs at '~/.clara/logs/'")
