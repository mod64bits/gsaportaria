from django.urls import path
from .views import SinglePostView

app_name = 'blog'

urlpatterns = [
    path('<slug:slug>/', SinglePostView.as_view(), name='singlepost'),
]
