__all__ = ["CreateNewAccount"]

from .usecase import Usecase
from app.accounts.models import Account


class CreateNewAccount(Usecase):
    def create_account(self, customer_id, name, email, phone_number, *args, **kwargs) -> Account:
        return self.account_repo.save_account(customer_id, name, email, phone_number)

    def execute(self, customer_id, name, email, phone_number, **kwargs):
        return self.create_account(customer_id, name, email, phone_number)
