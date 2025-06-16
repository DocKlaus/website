from sqlalchemy.orm import Mapped

from .base import Base


class Potato_gun(Base):

	name: Mapped[str]
	armor: Mapped[str]
	description: Mapped[str]

	dmg: Mapped[int]
	capacity_mag: Mapped[int]
	amount_mag: Mapped[int]
	recoil: Mapped[int]
	rof: Mapped[int]

