from django.urls import path
from pastes import views

app_name = 'pastes-app'
urlpatterns = [
    # path('', )
    path('', views.PasteListView.as_view(),
    name='list-pastes-view'),
    path(r'pastes/create/', views.CreatePasteView.as_view(),
    name='create-paste-view'),
    path('<slug>/', views.DetailPasteView.as_view(),
    name='detail-paste-view'),
    path('<slug>/update/', views.PasteUpdateView.as_view(),
    name='update-paste-view'),
    path('<slug>/delete/', views.PasteDeleteView.as_view(),
    name='delete-paste-view'),
]
