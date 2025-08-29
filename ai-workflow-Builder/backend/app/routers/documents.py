from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import uuid
router = APIRouter()

@router.post('/upload')
async def upload_document(file: UploadFile = File(...)):
    dest_dir = Path('/tmp/uploads')
    dest_dir.mkdir(parents=True, exist_ok=True)
    doc_id = str(uuid.uuid4())
    dest = dest_dir / f"{doc_id}_{file.filename}"
    content = await file.read()
    dest.write_bytes(content)
    # Return minimal metadata
    return {'id': doc_id, 'filename': file.filename, 'path': str(dest)}
