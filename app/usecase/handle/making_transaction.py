__all__ = ['MakingTransaction']

from .usecase import Usecase
from app.accounts.models.account import Account


class MakingTransaction(Usecase):
    def make_transaction(self, account_id, amount, transaction_type, *args, **kwargs) -> Account:
        account = self.account_repo.find_account_by_id(account_id)
        if not account:
            return
        else:
            if transaction_type == "deposit":
                account.deposit(amount)
            elif transaction_type == "withdraw":
                account.withdraw(amount)
            return account

    def execute(self, account_id, amount, transaction_type, **kwargs):
        return self.make_transaction(account_id, amount, transaction_type)
