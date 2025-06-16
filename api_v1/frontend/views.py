from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/weapons", response_class=HTMLResponse)
async def show_weapons(request: Request):
    return templates.TemplateResponse("weapons.html", {"request": request})