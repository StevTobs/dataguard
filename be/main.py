from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI()

templates = Jinja2Templates(
    directory=str(BASE_DIR / "fe")
)

class ProtectRequest(BaseModel):
    text: str

@app.get("/dataguard")
def ui(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/dataguard/protect")
def protect(req: ProtectRequest):
    protected = req.text.replace("John", "[NAME]")
    protected = protected.replace("0812345678", "[PHONE]")
    return {"protected": protected}