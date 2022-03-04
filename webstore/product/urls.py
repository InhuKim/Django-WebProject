from django.urls import path
from product import views
from django.views.generic import TemplateView

# http://127.0.0.1:8000/

app_name = 'product'

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:product_id>/', views.p_detail, name="p_detail"),
]
