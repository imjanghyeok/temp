from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # 127.0.0.1:8000
    path('blog/<int:blog_id>', views.detail, name='detail'),
    path('blog/new', views.new, name='new'),
    path('blog/create', views.create, name='create'),
    path('blog/edit/<int:blog_id>', views.edit, name='edit'),
    path('blog/update/<int:blog_id>', views.update, name='update'),
    path('blog/delete/<int:blog_id>', views.delete, name='delete'),
    path('blog/declaration/<int:blog_id>', views.declaration, name='declaration'),
    path('blog/declare/<int:blog_id>', views.declare, name='declare'),
    path('blog/search/', views.search, name='search'),
]
