
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'lessons'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('subjects/<int:subject_id>', views.subject, name = 'subject'),
    path('itype/<int:subject_id>/<int:itype_id>', views.itype, name = 'itype'),
    path('add_item_ajax', views.add_item_ajax, name="add_item_ajax"),
    path('add_itype_ajax', views.add_itype_ajax, name="add_itype_ajax"),
    path('delete_itype_ajax', views.delete_itype_ajax, name="delete_itype_ajax"),
    path('addblock_items_ajax', views.addblock_items_ajax, name="addblock_items_ajax"),
    path('delete_item_ajax', views.delete_item_ajax, name="delete_item_ajax"),
    path('load_item_ajax', views.load_item_ajax, name="load_item_ajax"),
]
