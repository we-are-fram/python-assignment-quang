__all__ = ['Usecase']

from app.usecase.abstractions import AbsUsecase
from app.accounts.managers.account import AccountManager


class Usecase(AbsUsecase):

    def __init__(self, account_repo):
        self.account_repo: AccountManager = account_repo
        super().__init__()

    def execute(self, *args, **kwargs):
        raise NotImplementedError('you must implement handle_message method')
