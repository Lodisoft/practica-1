from django.urls import path
from core.blog.views import *
from django.views.generic import TemplateView
from django.contrib import admin
from core.blog import views
app_name="blog"

urlpatterns = [
    path(route='',view=views.PostsFeedView.as_view(),name='index_blog'),
    path(route='posts/<slug:url>/',view=views.PostDetailView.as_view(),name='detail_post'),
    path(route='posts/save_comment', view=views.save_comment, name='save_comment'),
    path(route='login/', view=views.LoginView.as_view(), name='login_blog'),
    path(route='registro/', view=views.SignupView.as_view(), name='register_blog'),
    path(route='sobre-mi/', view=TemplateView.as_view(template_name='aboutBlog.html'), name='about_blog'),
    path(route='registro_completado/', view=TemplateView.as_view(template_name='registerokBlog.html'), name='registerok'),
    #path('inicio/', IndexTemplateView.as_view(), name="almacen_index"),
    #path('product/list/', ProductListView.as_view(), name="product_list"),
    #path('category/add/', CategoryCreateView.as_view(), name="category_create"),
    #path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name="category_update"),
    #path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name="category_delete"),
    #path('category/form/', CategoryFormView.as_view(), name="category_form")
]