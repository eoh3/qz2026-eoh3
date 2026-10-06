from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:pk>/delete/', views.article_soft_delete, name='article_soft_delete'),
    path('attachment/<int:pk>/download/', views.attachment_download, name='attachment_download'),
]
