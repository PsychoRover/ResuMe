from fastapi import APIRouter, UploadFile

router = APIRouter(prefix="/v1")


@router.post("/upload")
async def upload_cv(file: UploadFile):
    print(file.filename)
    return {"filename": file.read()}
