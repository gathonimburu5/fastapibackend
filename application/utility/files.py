import os
import uuid
from fastapi import UploadFile
from pathlib import Path

UPLOAD_FOLDER = Path("uploads/customerFiles")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

async def saveFiles(file: UploadFile):
    folder_path = UPLOAD_FOLDER
    folder_path.mkdir(parents=True, exist_ok=True)

    file_ext = os.path.splitext(file.filename)[1]
    unique_name = f"{uuid.uuid4()}{file_ext}"
    file_path = folder_path/unique_name

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    return unique_name