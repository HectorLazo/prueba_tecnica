from django.urls import path

from users_api import views

urlpatterns = [
	path('', views.apiOverView, name="api-overview"),
	path('usuario-list/', views.usuarioList, name="usuario-list"),
	path('usuario-detail/<str:pk>', views.usuarioDetail, name="usuario-detail"),
	path('usuario-update/<str:pk>', views.usuarioUpdate, name="usuario-update"),
	path('usuario-create/', views.usuarioCreate, name="usuario-create"),
	path('usuario-delete/<str:pk>', views.usuarioDelete, name="usuario-delete"),
]
