from fastapi import APIRouter, HTTPException, UploadFile, File
from client import supabase
import dotenv

router = APIRouter(prefix="/outputs", tags=["Outputs"])
supabase_url = dotenv.dotenv_values().get("SUPABASE_URL", "")

@router.post("/upload")
async def upload_file_to_data_source(file: UploadFile = File(...)):
    try:
        bucket_name = "outputs"
        file_content = await file.read()
        file_path = file.filename

        response = supabase.storage.from_(bucket_name).upload(
            file_path,
            file_content,
            {"content-type": file.content_type}
        )

        return {"message": "File uploaded successfully", "file": response.full_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download/{file_name}")
async def get_public_file_url(file_name: str):
    try:
        bucket_name = "outputs"
        public_url = f"{supabase_url}/storage/v1/object/public/{bucket_name}/{file_name}"

        return {"download_url": public_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
