from django.contrib import admin
from .models import Expense, Budget, Category

admin.site.register(Expense)
admin.site.register(Budget)
admin.site.register(Category)