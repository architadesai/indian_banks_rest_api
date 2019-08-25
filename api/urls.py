from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

# When access token expires, get new token using refresh token view
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/', include('bank.urls')),

    # For DRF's login (authenticating)
    path('api-auth/', include('rest_framework.urls')),

    # To get jwt token
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # To refresh/renew token once it expires
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]
