__all__ = ['AccountManager']


from django.db import models
from app.customer.models.customer import Customer


class AccountManager(models.Manager):
    """Custom manager for Account model"""

    def save_account(self, customer_id, name, email, phone_number, *args, **kwargs):
        customer = Customer.objects.filter(customer_id=customer_id).first()
        if not customer:
            customer = Customer.objects.create(
                customer_id=customer_id,
                name=name,
                email=email,
                phone_number=phone_number
            )
        account = self.model(
            customer=customer,
            balance=0,
            account_number='Account-' + str(self.all().count() + 1)
        )
        account.save()
        return account

    def find_account_by_id(self, account_id):
        return self.model.objects.filter(account_id=account_id).first()

    def find_accounts_by_customer_id(self, customer_id):
        return self.model.objects.filter(customer_id=customer_id).first()

    def get_all_accounts(self):
        return self.all()
