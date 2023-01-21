from schemas.sample import SampleTableItemCreate
from utils.app_exceptions import AppException

from services.main import AppService, AppCRUD
from models.foo import SampleItem
from utils.service_result import ServiceResult


class SampleAppService(AppService):
    def create_item(self, item: SampleTableItemCreate) -> ServiceResult:
        sample_item = SampleCRUD(self.db).create_item(item)
        if not sample_item:
            return ServiceResult(AppException.SampleException())
        return ServiceResult(sample_item)

    def get_item(self, item_id: int) -> ServiceResult:
        sample_item = SampleCRUD(self.db).get_item(item_id)
        if not sample_item:
            return ServiceResult(AppException.SampleException())
        if not sample_item.public:
            return ServiceResult(AppException.SampleException)
        return ServiceResult(sample_item)


class SampleCRUD(AppCRUD):
    def create_item(self, item: SampleTableItemCreate) -> SampleItem:
        sample_item = SampleItem(description=item.description, public=item.public)
        self.db.add(sample_item)
        self.db.commit()
        self.db.refresh(sample_item)
        return sample_item

    def get_item(self, item_id: int) -> SampleItem | None:
        sample_item = self.db.query(SampleItem).filter(SampleItem.id == item_id).first()
        if sample_item:
            return sample_item
        return None
