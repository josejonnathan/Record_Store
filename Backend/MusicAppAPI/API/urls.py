from . import views
from django.urls import path
from .views import AllRecordsView, RecordDetailView, CreateRecordsView, UpdateDeleteRecordsView, SimpleRecordsView

urlpatterns = [

    path('all/', AllRecordsView.as_view()),
    path('<int:pk>/', RecordDetailView.as_view()),
    path('create/', CreateRecordsView.as_view()),
    path('update/<int:pk>/', UpdateDeleteRecordsView.as_view()),
    path('simple/', SimpleRecordsView.as_view()),

]
