from django.urls import path
from .import views


urlpatterns= [
  path('',views.predict_d,name='predict_d'),
  path('eda/', views.eda_view, name='eda_page'),
]