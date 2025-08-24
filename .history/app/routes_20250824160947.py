from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.utils import process_text_file, add_document_to_store, search_documents

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")
    content = await file.read()
    text = process_text_file(content)
    add_document_to_store(text)
    return {"filename": file.filename, "size": len(content)}

@router.post("/query")
async def query_portal(req: QueryRequest):
    results = search_documents(req.query)
    return {"query": req.query, "results": results}
