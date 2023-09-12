from django.contrib import admin
from django.urls import path

from django_views_routing_homework.views.level_1.a_welcome_user import welcome_user_view
from django_views_routing_homework.views.level_1.b_bye_user import bye_user_view
from django_views_routing_homework.views.level_1.c_baned_username import is_username_banned_view
from django_views_routing_homework.views.level_1.d_user_info import get_user_info_view
from django_views_routing_homework.views.level_1.e_month_title import get_month_title_view
from django_views_routing_homework.views.level_2.a_user_info_by_username import get_user_info_by_username_view
from django_views_routing_homework.views.level_2.c_product_type import get_products_view
from django_views_routing_homework.views.level_2.d_authorization import authorization_view, process_authorization_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bye/', bye_user_view),
    path('welcome/', welcome_user_view),
    path('banned/<slug:username>/', is_username_banned_view),
    path('user-info/<int:user_id>/', get_user_info_view),
    path('month-title/<int:month_number>/', get_month_title_view),
    path('user-info-by-username/<int:username>/', get_user_info_by_username_view),
    path('products/', get_products_view),
    path('authorization/', authorization_view),
    path('process-authorization/', process_authorization_view),
    # добавлять пути тут
]
