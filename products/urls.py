from django.urls import path

from products.views import ProductsListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('', ProductsListView.as_view(), name='list')

]
