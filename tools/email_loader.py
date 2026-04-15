from imapclient import IMAPClient
import email
import os
from config import EMAIL_USER, EMAIL_PASS

def fetch_email_pdfs():
    paths = []
    os.makedirs("downloads", exist_ok=True)

    try:
        with IMAPClient("imap.gmail.com") as client:
            client.login(EMAIL_USER, EMAIL_PASS)
            client.select_folder("INBOX")

            messages = client.search(['UNSEEN'])

            for uid in messages:
                raw = client.fetch(uid, ['RFC822'])[uid][b'RFC822']
                msg = email.message_from_bytes(raw)

                for part in msg.walk():
                    if part.get_content_type() == "application/pdf":
                        filename = part.get_filename()
                        filepath = f"downloads/{filename}"

                        with open(filepath, "wb") as f:
                            f.write(part.get_payload(decode=True))

                        paths.append(filepath)

    except Exception as e:
        print("Email Error:", e)

    return paths