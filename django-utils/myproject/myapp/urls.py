from django.urls import path
from .views import (post_create, post_list, post_update, post_delete, post_detail,
                    PostCreateView, PostListView, PostUpdateView, PostDeleteView, PostDetailView)

urlpatterns = [
    
    
    path('fbv/', post_list, name='post_list'),
    path('fbv/create/', post_create, name='post_create'),
    path('fbv/detail/<int:pk>/', post_detail, name='post_detail'),
    path('fbv/update/<int:pk>/', post_update, name='post_update'),
    path('fbv/delete/<int:pk>/', post_delete, name='post_delete'),
    
    # Class-based views
    path('cbv/', PostListView.as_view(), name='post_list_cbv'),
    path('cbv/create/', PostCreateView.as_view(), name='post_create_cbv'),
    path('cbv/detail/<int:pk>/', PostDetailView.as_view(), name='post_detail_cbv'),
    path('cbv/update/<int:pk>/', PostUpdateView.as_view(), name='post_update_cbv'), 
    path('cbv/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete_cbv'),
]
