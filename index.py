import os
import requests

# ==== CONFIG ====
BOT_TOKEN = "8377097614:AAGt8MOFJfzdYCtpikwNK_noCsenKXVTUY0"   # 🔴 Replace with your bot token
CHAT_ID = "5933203565"   # 🔴 Replace with your Telegram chat ID
FILE_PATH = "/home/user/bigfile.zip"   # 🔴 Replace with the file you want to send
# ================

def send_file(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

    file_size = os.path.getsize(file_path)
    uploaded = 0
    chunk_size = 1024 * 1024  # 1MB chunks

    with open(file_path, "rb") as f:
        # Stream upload with chunks
        def file_gen():
            nonlocal uploaded
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                uploaded += len(data)
                percent = int((uploaded / file_size) * 100)
                print(f"\r📤 Uploading: {percent}% ({uploaded // (1024*1024)}MB/{file_size // (1024*1024)}MB)", end="")
                yield data

        response = requests.post(
            url,
            data={"chat_id": CHAT_ID},
            files={"document": (os.path.basename(file_path), file_gen())}
        )

    print("\n✅ Upload complete:", response.json())

if __name__ == "__main__":
    send_file(FILE_PATH)
