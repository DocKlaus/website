from pydantic import BaseModel, ConfigDict


class Potato_gun(BaseModel):

	name: str
	armor: str
	description: str

	dmg: int
	capacity_mag: int
	amount_mag: int
	recoil: int
	rof: int


class PotatoCreate(Potato_gun):
	pass


class PotatoUpdate(PotatoCreate):
	pass


class PotatoUpdatePartial(PotatoCreate):
	name: str | None = None
	armor: str | None = None
	description: str | None = None

	dmg: int | None = None
	capacity_mag: int | None = None
	amount_mag: int | None = None
	recoil: int | None = None
	rof: int | None = None


class Potato(Potato_gun):
	model_config = ConfigDict(from_attributes = True)

	id: int