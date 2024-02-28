__all__ = ["GeneratingAccountStatments"]

from .usecase import Usecase


class GeneratingAccountStatments(Usecase):
    def generating_account_statment(self, account_id, *args, **kwargs):
        account = self.account_repo.find_account_by_id(account_id)
        # Simplified statement generation, could fetch transaction details from database
        statement = f"Account Statement for Account: {account.account_number}\n"
        statement += f"Current Balance: {account.get_balance()}\n"
        # Add more transaction details here
        return statement

    def execute(self, account_id, *args, **kwargs):
        return self.generating_account_statment(account_id)
