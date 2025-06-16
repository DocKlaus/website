from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime
import uvicorn

app = FastAPI()

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "time": curr_time}
    )

@app.get("/potatoes", response_class=HTMLResponse)
async def second_page(request: Request):
    return templates.TemplateResponse(
        "potatoes.html",
        {"request": request, "message": "Это станица с картошко-пушками"}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)