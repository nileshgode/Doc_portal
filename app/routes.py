from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

# Simple route for document upload (store file temporarily)
@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")
    # For now, just read file content and return filename and size
    content = await file.read()
    return {"filename": file.filename, "size": len(content)}

# Simple route for query placeholder
@router.post("/query")
async def query_portal(query: str):
    # Placeholder response; will connect to AI model later
    return {"query": query, "response": "This is a stub for AI response."}
