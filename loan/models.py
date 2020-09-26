from django.db import models
from django.contrib.auth.models import User


LOAN_AMOUNT = [
        ("10,000", "N10,000"),
        ("20,000", "N20,000"),
        ("30,000", "N30,000"),
        ("40,000", "N40,000"),
        ("50,000", "N50,000"),
        ("60,000", "N60,000"),
        ("70,000", "N70,000"),
        ("80,000", "N80,000"),
        ("90,000", "N90,000"),
        ("100,000", "N100,000"),
        ("200,000", "N200,000"),
        ("300,000", "N300,000"),
        ("400,000", "N400,000"),
        ("500,000", "N500,000"),
        ("600,000", "N600,000"),
        ("700,000", "N700,000"),
        ("800,000", "N800,000"),
        ("900,000", "N900,000"),
        ("1,000,000", "N1,000,000"),
]




class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone = models.PositiveIntegerField()
    loan_amount = models.CharField(choices=LOAN_AMOUNT, max_length=12)
    bvn = models.PositiveIntegerField()
    bank = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)
    account_number = models.PositiveIntegerField()
    app_date = models.DateField(auto_now=True)
    paid = models.BooleanField(default=False)

    #upload id card
    #upload passport

    def __str__(self):
        return self.first_name


