from django.urls import path

from main import views

urlpatterns = [
    path('', views.ProcessesView.as_view(), name='processes'),
    path('<int:pk>', views.ProcessView.as_view(), name='process'),
]
