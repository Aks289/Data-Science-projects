from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os

def fetch_drive_pdfs():
    creds = Credentials.from_authorized_user_file('token.json')
    service = build('drive', 'v3', credentials=creds)

    results = service.files().list(
        q="mimeType='application/pdf'",
        fields="files(id,name)"
    ).execute()

    files = results.get('files', [])
    paths = []

    os.makedirs("downloads", exist_ok=True)

    for file in files:
        request = service.files().get_media(fileId=file['id'])
        path = f"downloads/{file['name']}"

        with open(path, "wb") as f:
            f.write(request.execute())

        paths.append(path)

    return paths