from django.urls import path

from REST.views import *

urlpatterns = [
    path('1', Products.as_view()),
    path('2/<int:pid>', Products.as_view()),
    path('3', ProductsJR.as_view()),
    path('4/<int:pk>', ProductsJRDetail.as_view()),
    path('5', ProductS.as_view()),
    path('6/<int:pk>', ProductSDetail.as_view()),
    path('get_prod/', get_prod),
    path('get_prod/<int:pid>', get_prodit),
]
