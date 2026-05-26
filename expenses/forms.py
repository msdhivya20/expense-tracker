from django import forms
from .models import Expense
from .models import Budget
from .models import Category

from django import forms

from .models import (
    Expense,
    Budget,
    Category
)


class ExpenseForm(forms.ModelForm):

    def __init__(self, *args, user=None, **kwargs):

        super().__init__(*args, **kwargs)

        if user:

            self.fields[
                'category'
            ].queryset = Category.objects.filter(
                user=user
            )

    class Meta:

        model = Expense

        fields = [

            'title',
            'amount',
            'category',
            'expense_date'

        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Expense Title'
                }
            ),

            'amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Amount'
                }
            ),

            'category': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'expense_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

        }



class BudgetForm(forms.ModelForm):

    class Meta:

        model = Budget

        fields = [

            "budget_amount"

        ]

        widgets = {

            "budget_amount": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter Monthly Budget"

                }

            )

        }


class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category

        fields = [

            'name'

        ]

        widgets = {

            'name': forms.TextInput(

                attrs={

                    'class': 'form-control',

                    'placeholder': 'Enter Category Name'

                }

            )

        }