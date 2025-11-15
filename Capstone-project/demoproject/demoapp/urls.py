
from django.urls import path
from . import views
urlpatterns = [
    path('user/', views.UserViewSet.as_view(), name='user' ),
]
