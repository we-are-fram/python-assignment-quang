import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

from app.usecase.handle.making_transaction import MakingTransaction
from app.usecase.handle.generating_account_statments import GeneratingAccountStatments
from app.usecase.handle.create_new_account import CreateNewAccount
from unittest.mock import Mock
from django.test import TestCase
import pytest


class TestCreateNewAccount(TestCase):
    def setUp(self):
        self.account_repo = Mock()
        self.usecase = CreateNewAccount(self.account_repo)

    @pytest.mark.django_db
    def test_execute(self):
        customer_id = 1
        name = 'John Doe'
        email = 'john.doe@example.com'
        phone_number = '1234567890'
        print('Account Repo: ', self.account_repo)
        account = self.usecase.execute(customer_id, name, email, phone_number)
        print(' Account: ', account)

        self.account_repo.save_account.assert_called_once_with(
            customer_id, name, email, phone_number)
        self.assertEqual(account, self.account_repo.save_account.return_value)


class TestGeneratingAccountStatments(TestCase):
    def setUp(self):
        self.account_repo = Mock()
        self.usecase = GeneratingAccountStatments(self.account_repo)

    @pytest.mark.django_db
    def test_execute(self):
        account_id = 1
        self.account_repo.find_account_by_id.return_value = Mock(
            account_number='123456', get_balance=Mock(return_value=1000))
        statement = self.usecase.execute(account_id)

        self.account_repo.find_account_by_id.assert_called_once_with(
            account_id)
        self.assertIn('Account Statement for Account: 123456', statement)
        self.assertIn('Current Balance: 1000', statement)


class TestMakingTransaction(TestCase):
    def setUp(self):
        self.account_repo = Mock()
        self.usecase = MakingTransaction(self.account_repo)

    @pytest.mark.django_db
    def test_execute(self):
        account_id = 1
        amount = 100
        transaction_type = 'deposit'
        self.account_repo.find_account_by_id.return_value = Mock(
            account_number='123456', get_balance=Mock(return_value=1000))
        expected_transaction = Mock()
        self.account_repo.make_transaction.return_value = expected_transaction
        transaction = self.usecase.execute(
            account_id, amount, transaction_type)

        self.account_repo.find_account_by_id.assert_called_once_with(
            account_id)
