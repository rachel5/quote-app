from django.urls import path

from . import views

urlpatterns = [
  path('', views.quote_list, name='quote_list'),
  path('quote/<int:pk>/', views.quote_detail, name='quote_detail'),
  path('quote/new', views.quote_new, name='quote_new'),
  path('quote/<int:pk>/edit/', views.quote_edit, name='quote_edit'),
  path('drafts/', views.quote_draft_list, name='quote_draft_list'),
  path('quote/<pk>/publish/', views.quote_publish, name='quote_publish'),
  path('quote/<pk>/remove/', views.quote_remove, name='quote_remove'),
]
