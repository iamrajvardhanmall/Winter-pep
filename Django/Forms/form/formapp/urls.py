from .views import form, Raj, edit_note, delete_note
from django.urls import path

urlpatterns = [
    path('', Raj),
    path('form/', form, name="form_save_data"),
    path('edit/<int:note_id>/', edit_note, name="edit_note"),
    path('delete/<int:note_id>/', delete_note, name="delete_note"),
]
