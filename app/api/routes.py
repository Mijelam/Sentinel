from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def ping():
    return {"status": "ok", "message": "Sentinel API running"}
