from django.urls import path, include

from users.views import CustomLoginView, UserRegisterView, UserLogoutView, UserUpdateView, \
    UserDeleteView, details_user

urlpatterns = (
    path('login/', CustomLoginView.as_view(), name='login_user'),
    path('register/', UserRegisterView.as_view(), name='register_user'),
    path('logout/', UserLogoutView.as_view(), name='logout_user'),
    path('<int:pk>/', include([
        path('', details_user, name='details_user'),
        path('edit/', UserUpdateView.as_view(), name='update_user'),
        path('delete/', UserDeleteView.as_view(), name='delete_user'),
    ]))
)