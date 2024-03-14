from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('home',views.homepage,name='home'),
    path('setup-camera',views.setup_camera,name='setup-camera'),
    path('setup-animal',views.animal_setup,name='setup_animal'),
    #path('google-auth',views.google_auth,name='google_auth'),
    #path('authenticated',views.authenticated,name='authenticated')
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]