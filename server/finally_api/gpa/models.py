from decimal import Decimal
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models, transaction


# Create your models here.
class Account(models.Model):
    account_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0))
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")

    def account_number(self):
        return str(self.id).zfill(12)


class Transaction(models.Model):
    CREDIT = 'CREDIT'
    DEBIT = 'DEBIT'
    TRANSACTION_TYPES = ((CREDIT, CREDIT), (DEBIT, DEBIT))

    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
    note = models.CharField(max_length=50, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0))
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")

    def _update_account_balance(self) -> None:
        if self.transaction_type == self.DEBIT:
            self.amount *= -1

        self.account_id.current_balance += self.amount

    @transaction.atomic
    def save(self, *args, **kwargs):
        self._update_account_balance()
        super(Transaction, self).save(*args, **kwargs)
        self.account_id.save()
