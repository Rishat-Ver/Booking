from pydantic import BaseModel


class SHotel(BaseModel):

    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int