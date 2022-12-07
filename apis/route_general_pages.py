#route_general_pages.py

from fastapi import APIRouter, Depends
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter(
    tags=["Homepage WEB"],
)

@general_pages_router.get("/page")
def home_UNDERDEV(request: Request):
	return templates.TemplateResponse("general_pages/homepage.html",{"request":request})