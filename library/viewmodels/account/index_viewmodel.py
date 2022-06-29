from library.viewmodels.shared.viewmodelbase import ViewModelBase
from library.services import user_service


class IndexViewModel(ViewModelBase):
    def __int__(self):
        super().__init__()
        self.user = user_service.find_user_by_id(self.user_id)

