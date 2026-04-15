import os
from imapclient import IMAPClient
import email
from config import EMAIL_USER, EMAIL_PASS

# 📁 LOCAL FILES
def load_from_local():
    folder = "data/downloads"
    files = []

    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            files.append(os.path.join(folder, file))

    return files


# 📧 EMAIL
import os
import email
import socket
from imapclient import IMAPClient
from config import EMAIL_USER, EMAIL_PASS

def load_from_email():
    os.makedirs("data/downloads", exist_ok=True)
    paths = []

    # ✅ Prevent hanging
    socket.setdefaulttimeout(20)

    try:
        print("🔌 Connecting to email...")

        with IMAPClient("imap.gmail.com") as client:
            client.login(EMAIL_USER, EMAIL_PASS)
            client.select_folder("INBOX")

            # ✅ Limit to 1 unread email (FAST)
            messages = client.search(['UNSEEN'])[:1]

            print(f"📩 Found {len(messages)} unread email(s)")

            for uid in messages:
                print("📥 Fetching email...")

                # ✅ Faster fetch (instead of RFC822)
                raw = client.fetch([uid], ['RFC822'])

                msg_data = raw[uid][b'RFC822']
                msg = email.message_from_bytes(msg_data)

                for part in msg.walk():
                    for part in msg.walk():
                        filename = part.get_filename()

    # ✅ Check by filename instead of content-type
                        if filename and filename.lower().endswith(".pdf"):

                            filepath = os.path.join("data/downloads", filename)

                            print(f"⬇️ Downloading: {filename}")

                            with open(filepath, "wb") as f:
                                f.write(part.get_payload(decode=True))

                            paths.append(filepath)

                # ✅ Mark email as read (avoid reprocessing)
                client.add_flags(uid, ['\\Seen'])

    except Exception as e:
        print("❌ Email Error:", e)

    return paths


# ☁️ GOOGLE DRIVE (Basic version using file path for now)
def load_from_gdrive():
    print("👉 Enter Google Drive file path (after download):")
    path = input("Path: ")

    if os.path.exists(path):
        return [path]
    else:
        print("File not found!")
        return []