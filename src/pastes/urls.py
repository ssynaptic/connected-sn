from django.urls import path
from pastes import views

app_name = 'pastes'
urlpatterns = [
    # path('', )
    path('', views.PasteListView.as_view(),
    name='list-pastes-views'),
    path(r'pastes/create/', views.CreatePasteView.as_view(),
    name='create-paste-view'),
]