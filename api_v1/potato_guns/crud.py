"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Potato_gun

from .schemas import PotatoCreate, PotatoUpdate, PotatoUpdatePartial

async def get_potatoes(session: AsyncSession) -> list[Potato_gun]:
    stmt = select(Potato_gun).order_by(Potato_gun.id)
    result: Result = await session.execute(stmt)
    potatoes = result.scalars().all()
    return list(potatoes)


async def get_potato(session: AsyncSession, potato_id: int) -> Potato_gun | None:
    return await session.get(Potato_gun, potato_id)


async def create_potato(session: AsyncSession, potato_in: PotatoCreate) -> Potato_gun:
    potato = Potato_gun(**potato_in.model_dump())
    session.add(potato)
    await session.commit()
    # await session.refresh(potato)
    return potato


async def update_potato(
		session: AsyncSession,
		potato: Potato_gun,
		potato_update: PotatoUpdate |PotatoUpdatePartial,
		partial: bool = False
) -> Potato_gun:
	for name, value in potato_update.model_dump(exclude_unset = partial).items():
		setattr(potato, name, value)
	await session.commit()
	return potato


async def delete_potato(
		session: AsyncSession,
		potato: Potato_gun
) -> None:
	await session.delete(potato)
	await session.commit()