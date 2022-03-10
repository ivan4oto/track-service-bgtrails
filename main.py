from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from services import get_static_image_url, upload_to_s3


class UploadFile(BaseModel):
    file_url: str
    bucket: Optional[str] = None
    path: Optional[str] = None


app = FastAPI()

@app.get("/static-image/")
async def get_static_image(jsonUrl: str):
    img_url = get_static_image_url(jsonUrl)
    return {
        "static_img_url": img_url,
    }


@app.post("/upload-to-s3/")
async def upload_to_s3(uploadFile: UploadFile):
    upload_to_s3(uploadFile.file_url, uploadFile.bucket, uploadFile.path)
    return uploadFile