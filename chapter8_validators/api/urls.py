from django.urls import path, include
from watchlist_app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# Using ViewSet
router.register(r"watchlist-viewset1", views.WatchListViewSet1)

urlpatterns = [   
    # Using ViewSet
    path("", include(router.urls)),
    
]
