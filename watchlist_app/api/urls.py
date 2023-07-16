from django.urls import path, include
from watchlist_app.api import views

urlpatterns = [
    path('watchlist-cbv-try1/', views.WatchlistCBView1.as_view(), name="watchlist-cbv-try1"),
    path('watchlist-detail-cbv-try1/<int:pk>/', views.WatchlistDetailCBView1.as_view(), name="watchlist-detail-cbv-try1"),
    path('reviewlist-cbv-try1/', views.ReviewlistCBView1.as_view(), name="reviewlist-cbv-try1"),
    path('streamplatform-detail-cbv-try1/<int:pk>/', views.StreamPlatformDetailView1.as_view(), name="streamplatform-detail-cbv-try1"),
    
]
