from django.urls import path
from .views import bottle_list, bottle_create, bottle_edit, bottle_delete, calculate_remaining
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', bottle_list, name='bottle_list'),  # Список всех бутылок
    path('create/', views.bottle_create, name='bottle_create'),  # Страница для создания бутылки
    path('edit/<int:pk>/', views.bottle_edit, name='bottle_edit'),  # Страница для редактирования бутылки
    path('delete/<int:pk>/', bottle_delete, name='bottle_delete'), # Удаление
    path('calculate/<int:bottle_id>/', calculate_remaining, name='calculate_remaining'),  # Страница для расчёта оставшегося объёма
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)