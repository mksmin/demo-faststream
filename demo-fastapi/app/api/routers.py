from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["main"])


@router.get("/")
async def test():
    return {"message": "Hello World"}
