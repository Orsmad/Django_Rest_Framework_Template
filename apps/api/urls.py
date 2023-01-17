from django.urls import re_path
from apps.api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    re_path(r'^api/profiles/$', views.profile_list),
    re_path(r'^api/profiles\/(?P<pk>.+)', views.prodile_detail),

    re_path(r'^api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

     re_path(r'^api/products/$', views.product_list),
    re_path(r'^api/products\/(?P<pk>.+)', views.product_detail),

]
   

    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
