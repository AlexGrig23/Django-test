
from django.urls import path

from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, GroupCreateView, GroupUpdateView, \
    GroupDeleteView, GroupListView

urlpatterns = [
    path('', UserListView.as_view(), name='users_list'),
    path('users/create/', UserCreateView.as_view(), name='create_user'),
    path('users/<int:pk>/', UserUpdateView.as_view(), name='edit_user'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='delete_user'),
    path('groups/', GroupListView.as_view(), name='groups_list'),
    path('groups/create/', GroupCreateView.as_view(), name='create_group'),
    path('groups/<int:pk>/', GroupUpdateView.as_view(), name='edit_group'),
    path('groups/<int:pk>/delete/', GroupDeleteView.as_view(), name='delete_group'),

]
