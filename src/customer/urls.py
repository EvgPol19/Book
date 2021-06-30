from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserCreateView.as_view(), name='registration'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    # path('profile/', views.UserProfileRegisterView.as_view(), name='profile'),
    path('profile_detail/<int:pk>/', views.UserProfileDetailView.as_view(), name='profile_detail'),
    path('profile_update/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('user_update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('user_update/', views.ProfileCreateView.as_view(), name = 'user_update'),
    # path('add_profile_update/<int:pk>/', views.UserAddUpdateView.as_view(), name = 'add_profile_update'),
    path('change_password/', views.UserPasswordChangeView.as_view(), name='change_password'),
    path('change_password_done/', views.UserPasswordChangeDoneView.as_view(), name='change_password_done'),
]