from fastapi import APIRouter

router = APIRouter()


@router.post("/optimize")
async def optimize(data: dict):

    content = data.get("content", "")

    return {
        "success": True,
        "data": {
            "original": content,
            "facebook": f"{content} #ScanForSafe",
            "instagram": f"{content} #Emergency",
            "twitter": f"{content[:180]}",
            "linkedin": f"{content}",
            "whatsapp": f"{content}",
            "youtube": f"{content}"
        }
    }