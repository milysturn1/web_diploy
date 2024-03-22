from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', category_page_view, name='category'),
    path('article/<int:article_id>/', article_detail_view, name='article_detail'),

    path('about_us/', about_us_page_view, name='about_us'),
    path('our_team/', our_teams_page_view, name='our_team'),
    path('services/', our_services_page_view, name='services'),

    path('add_article/', add_article, name='add_article'),

    path('register/', register_user_view, name='register'),
    path('login/', login_user_view, name='login'),
    path('logout/', logout_user_view, name='logout'),

    path('update_article/<int:article_id>/', update_article_view,
         name='update_article'),
    path('delete_article/<int:article_id>/', article_delete,
         name='delete_article'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('edit_user/<int:user_id>/', update_profile_view,
         name="update_profile"),
    path("save_comment/<int:article_id>/", save_comment,
         name="save_comment")
]
