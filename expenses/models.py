from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Expense(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=100
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,   # changed
        null=True,
        blank=True
    )

    expense_date = models.DateField()

    def __str__(self):
        return self.title





class Budget(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    month = models.DateField()

    budget_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    carry_forward = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    total_budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    spent = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    remaining = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ["-month"]

    def __str__(self):

        return f"{self.user.username} - {self.month}"