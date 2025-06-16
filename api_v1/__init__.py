from fastapi import APIRouter

from .potato_guns.views import router as potato_router

router = APIRouter()
router.include_router(router = potato_router, prefix = '/potatoes')