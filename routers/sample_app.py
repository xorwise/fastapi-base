from fastapi import APIRouter, Depends

from services.sample import SampleAppService
from schemas.sample import SampleItem, SampleTableItemCreate

from utils.service_result import handle_result

from config.database import get_db

router = APIRouter(
    prefix="/sample",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.post("/item/", response_model=SampleItem)
async def create_item(item: SampleTableItemCreate, db: get_db = Depends()):
    result = SampleAppService(db).create_item(item)
    return handle_result(result)


@router.get("/item/{item_id}", response_model=SampleItem)
async def get_item(item_id: int, db: get_db = Depends()):
    result = SampleAppService(db).get_item(item_id)
    return handle_result(result)
