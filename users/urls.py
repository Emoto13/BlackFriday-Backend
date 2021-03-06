from django.urls import path

from users.views import authenticated_user_information, create_user, update_user, delete_user, get_user, search_users

user_urls = [
    path('', authenticated_user_information),
    path('create/', create_user),
    path('update/', update_user),
    path('delete/', delete_user),
    path('<str:username>/', get_user),
    path('search/<str:query>/', search_users),
]
