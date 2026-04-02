from fastapi import APIRouter, Request, Query, HTTPException
from config import VERIFY_TOKEN
from services.instagram import send_dm, reply_to_comment
from services.config_manager import get_reel_config

router = APIRouter(prefix="/webhook", tags=["webhook"])

@router.get("")
async def verify_webhook(
    hub_mode: str = Query(alias="hub.mode"),
    hub_verify_token: str = Query(alias="hub.verify_token"),
    hub_challenge: str = Query(alias="hub.challenge")
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)
    raise HTTPException(status_code=403, detail="Verification failed")

@router.post("")
async def handle_webhook(request: Request):
    body = await request.json()
    
    if body.get("object") != "instagram":
        return {"status": "ignored"}
    
    for entry in body.get("entry", []):
        for change in entry.get("changes", []):
            if change.get("field") == "comments":
                value = change.get("value", {})
                comment_id = value.get("id")
                comment_text = value.get("text", "").strip().lower()
                media_id = value.get("media", {}).get("id")
                
                if not comment_id or not media_id:
                    continue
                
                config = get_reel_config(media_id)
                
                if not config.get("active"):
                    continue
                
                trigger = config.get("trigger_keyword", "").lower()
                if trigger and trigger in comment_text:
                    dm_message = config.get("dm_message", "")
                    comment_reply = config.get("comment_reply", "")
                    
                    if dm_message:
                        send_dm(comment_id, dm_message)
                    
                    if comment_reply:
                        reply_to_comment(comment_id, comment_reply)
    
    return {"status": "ok"}
