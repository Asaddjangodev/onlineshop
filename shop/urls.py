from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_lists'),  # product_list view without any parameters
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    # provides a category_slug parameter to the view for filtering products according to a given category
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
