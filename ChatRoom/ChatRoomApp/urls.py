from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', views.MessagesCreateView, basename='messages')

urlpatterns = [

    path('messages/', views.MessagesView.as_view()),
    path('messages/single/<int:pk>/', views.MessagesSingleView.as_view()),
    path('messages/list/<int:id>/', views.MessagesListView.as_view()),
    path('messages/create/', include(router.urls)),

]