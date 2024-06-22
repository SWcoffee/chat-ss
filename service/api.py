import json

from fastapi import APIRouter, Header, HTTPException, Depends, Form
from config.config import AUTH_KEY, REDIS_CON
from model.model import SessionModel, AddSessionIn
from model.model_data import common_model, plus_model, user_model
from tools.rt2at import get_access_token

router = APIRouter()


async def verify_header(authkey: str = Header(...)):
    if authkey != AUTH_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")


@router.post("/getsession", response_model=dict, dependencies=[Depends(verify_header)])
def get_session(email: str = Form(...)):
    session = REDIS_CON.get("account:" + email)
    if session is None:
        raise HTTPException(status_code=404, detail="session not found")
    return json.loads(session)


@router.post("/addsession", response_model=str, dependencies=[Depends(verify_header)])
def add_session(session: AddSessionIn):
    email = session.email
    model_data = session.model_dump(exclude={"email", "isPlus"})
    model_data["user"] = json.loads(user_model)["user"]
    model_data["user"]["email"] = email
    model_data["user"]["name"] = email
    model_data["models"] = json.loads(common_model)["models"]
    if session.isPlus:
        model_data["models"] = json.loads(plus_model)

    REDIS_CON.set("account:" + email, json.dumps(model_data))
    return "success"


@router.post("/refreshsession", response_model=dict, dependencies=[Depends(verify_header)])
async def refresh_session(email: str = Form(...), refreshCookie: str = Form(...)):
    session_data = REDIS_CON.get("account:" + email)
    if session_data is None:
        raise HTTPException(status_code=404, detail="session not found")

    session_data = json.loads(session_data)
    rt = refreshCookie
    access_token = await get_access_token(rt)
    if access_token is None:
        if session_data and session_data.get("refreshCookie"):
            rt = session_data.get("refreshCookie")
            access_token = await get_access_token(rt)
        else:
            raise HTTPException(status_code=400, detail="refresh error")

    session_data["accessToken"] = access_token
    session_data["refreshCookie"] = rt
    REDIS_CON.set("account:" + email, json.dumps(session_data))
    return session_data
