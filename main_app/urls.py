from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='update'),
    path('finches/<int:pk>/delete/',
         views.FinchDelete.as_view(), name='finch_delete'),
    path('finches/<int:finch_id>/add_seen/',views.add_seen, name="add_seen"),
    path('finches/<int:finch_id>/assoc_tree/<int:tree_id>/',views.assoc_tree, name="assoc_tree")
]
