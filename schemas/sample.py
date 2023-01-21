from pydantic import BaseModel


class SampleItemBase(BaseModel):
    description: str


class SampleTableItemCreate(SampleItemBase):
    public: bool


class SampleItem(SampleItemBase):
    id: int

    class Config:
        orm_mode = True
