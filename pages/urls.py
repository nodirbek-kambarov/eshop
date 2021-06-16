from django.urls import path
from pages.views import ContactCreateView, HomeView, AboutView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),
]
