from django.template.defaulttags import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from REST.views import *

router = routers.DefaultRouter()
router.register('prod', ProductS)
print(router.urls)
urlpatterns = [
    path('1', Products.as_view()),
    path('2/<int:pid>', Products.as_view()),
    path('3', ProductsJR.as_view()),
    path('4/<int:pk>', ProductsJRDetail.as_view()),
    path('get_prod/', get_prod),
    path('get_prod/<int:pid>', get_prodit),
    path('5/', include(router.urls)),
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth-drf/', include('rest_framework.urls')),
]
