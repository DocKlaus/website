from fastapi import APIRouter

from .potato_guns.views import router as potato_router
from .frontend.views import router as frontend_router

router = APIRouter()
router.include_router(router = potato_router, prefix = '/potatoes')
router.include_router(router = frontend_router)