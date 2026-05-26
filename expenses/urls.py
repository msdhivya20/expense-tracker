from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('add-expense/', views.add_expense, name='add_expense'),

    path(
        'update-expense/<int:id>/',
        views.update_expense,
        name='update_expense'
    ),

    path(
        'delete-expense/<int:id>/',
        views.delete_expense,
        name='delete_expense'
    ),

    path(
    'export-excel/',
    views.export_excel,
    name='export_excel'
),

path(
    'export-pdf/',
    views.export_pdf,
    name='export_pdf'
),

path(
    'set-budget/',
    views.set_budget,
    name='set_budget'
),

   path(
        'category-analytics/',
        views.category_analytics,
        name='category_analytics'
    ),

    

    path('expense_comparison/', 
    views.expense_comparison, 
    name='expense_comparison'),

    path(
    'categories/',
    views.category_list,
    name='category_list'
    ),

    path(
    'delete-category/<int:id>/',
    views.delete_category,
    name='delete_category'
    ),

    path(
    "report/",
    views.report,
    name="report"
),

path(
    "export-category-excel/",
    views.export_category_excel,
    name="export_category_excel"
),

path(
    "export-category-pdf/",
    views.export_category_pdf,
    name="export_category_pdf"
),
]