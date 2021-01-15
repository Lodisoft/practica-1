from django.urls import path
from core.almacen.views import *

app_name="almacen"

urlpatterns = [
    path('inicio/', IndexTemplateView.as_view(), name="almacen_index"),
    path('product/list/', ProductListView.as_view(), name="product_list"),
    #path('category/add/', CategoryCreateView.as_view(), name="category_create"),
    #path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name="category_update"),
    #path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name="category_delete"),
    #path('category/form/', CategoryFormView.as_view(), name="category_form")
]