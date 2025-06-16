from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession


from core.models import db_helper, Potato_gun

from . import crud


async def get_potato_by_id(
		potato_id: Annotated[int, Path],
		session: AsyncSession = Depends(db_helper.scoped_session_dependency),
		) -> Potato_gun:
	potato = await crud.get_potato(session = session, potato_id = potato_id)
	if potato is not None:
		return potato
	raise HTTPException(
		status_code = status.HTTP_400_BAD_REQUEST,
		detail = f"Potato gun {potato_id} not found",
		)