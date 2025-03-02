from django.urls import path
from . import views
urlpatterns=[
    path('',views.UserPanelDashboardPage.as_view(), name='user_panel'),
    path('change-password-page', views.ChangePassword.as_view(), name='change_password_page'),
    path('edit-profile',views.EditUserProfilePage.as_view(), name='edit_profile_page'),
    path('user-basket', views.user_basket, name='user_basket_page')
]