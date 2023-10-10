from django.db import models

#FROM MODELS OTHER APPS
from apps.users.models import User
from apps.books.models import Copy

# Create your models here.
class Loan(models.Model):
    date_loan = models.DateTimeField()
    date_end = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    copy = models.ForeignKey(Copy, on_delete=models.DO_NOTHING)