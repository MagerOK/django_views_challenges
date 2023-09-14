from django.contrib import admin
from django.urls import path

from django_views_routing_homework.views.level_1.a_welcome_user import welcome_user_view
from django_views_routing_homework.views.level_1.c_baned_username import is_username_banned_view
from django_views_routing_homework.views.level_2.a_user_info_by_username import get_user_info_by_username_view
from django_views_routing_homework.views.level_2.b_greet_user_language import greet_user_in_different_languages_view
from django_views_routing_homework.views.level_2.c_product_type import get_products_view
from django_views_routing_homework.views.level_2.d_authorization import authorization_view, process_authorization_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome_user_view),
    path('banned/<slug:username>/', is_username_banned_view),
    path('user-info-by-username/<slug:username>/', get_user_info_by_username_view),
    path('products/', get_products_view),
    path('authorization/', authorization_view),
    path('process-authorization/', process_authorization_view),
    path('greet/<slug:name>/<slug:language>/', greet_user_in_different_languages_view),
]
