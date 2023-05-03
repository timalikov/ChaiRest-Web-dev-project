from django.urls import path, include

from . import views
from views import *
# from views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )



urlpatterns = [
    path('category/', views.categories_list),
    path('category/<int:id>/', views.category_detail),
    path('category/<int:id>/furniture/', views.category_furniture),
    path('furniture/', views.furniture_list),
    # path('auth/login/', TokenObtainPairView.as_view(), name='jwt-obtain-token'),
    # path('auth/refresh/', TokenRefreshView.as_view(), name='jwt-refresh-token'),
    # path('auth/verify/', TokenVerifyView.as_view(), name='jwt-verify-token'),
]
