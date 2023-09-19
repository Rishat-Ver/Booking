from app.hotels.rooms.models import Rooms
from app.dao.base import BaseDAO


class RoomDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def find_all():
        ...
