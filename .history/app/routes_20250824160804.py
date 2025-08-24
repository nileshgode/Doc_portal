from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils import process_text_file, add_document_to_store

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")
    content = await file.read()
    text = process_text_file(content)
    add_document_to_store(text)
    return {"filename": file.filename, "size": len(content)}
