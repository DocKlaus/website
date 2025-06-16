from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Potato_gun, PotatoCreate, PotatoUpdate, PotatoUpdatePartial
from .dependencies import get_potato_by_id
from core.models import db_helper

router = APIRouter(tags=["Potato"])


@router.get('/', response_model=list[Potato_gun])
async def get_potato(
		session: AsyncSession = Depends(db_helper.scoped_session_dependency),
		):
	return await crud.get_potatoes(session = session)


@router.post(
	'/',
	response_model=Potato_gun,
	status_code=status.HTTP_201_CREATED,
	)
async def create_potato(
		potato_in: PotatoCreate,
		session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        ):
	return await crud.create_potato(potato_in = potato_in, session = session)


@router.get('/{potato_id}/', response_model=Potato_gun)
async def get_potato(
		potato: Potato_gun = Depends(get_potato_by_id),
		):
	return potato

@router.put('/{potato_id}/')
async def update_potato(
		potato_update: PotatoUpdate,
		potato: Potato_gun = Depends(get_potato_by_id),
		session: AsyncSession = Depends(db_helper.scoped_session_dependency),
		):
	return await crud.update_potato(
		session = session,
		potato = potato,
		potato_update = potato_update,
		)


@router.patch('/{potato_id}/')
async def update_potato_partial(
		potato_update: PotatoUpdatePartial,
		potato: Potato_gun = Depends(get_potato_by_id),
		session: AsyncSession = Depends(db_helper.scoped_session_dependency),
		):
	return await crud.update_potato(
		session = session,
		potato = potato,
		potato_update = potato_update,
		partial = True
		)

@router.delete('/{potato_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_potato(
		potato:Potato_gun = Depends(get_potato_by_id),
		session: AsyncSession = Depends(db_helper.scoped_session_dependency),
		) -> None:
	await crud.delete_potato(session = session, potato = potato)