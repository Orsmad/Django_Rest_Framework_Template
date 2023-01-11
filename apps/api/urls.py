from django.urls import re_path
from apps.api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
   
    re_path(r'^api/profiles/$', views.profile_list),
    re_path(r'^api/profiles\/(?P<pk>.+)', views.profile_detail),

    re_path(r'^api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
   