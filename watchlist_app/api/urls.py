from django.urls import path, include
from watchlist_app.api import views

urlpatterns = [
    # Watchlist urls
    path('watchlist-cbv-try1/', views.WatchlistCBView1.as_view(), name="watchlist-cbv-try1"),
    path('watchlist-detail-cbv-try1/<int:pk>/', views.WatchlistDetailCBView1.as_view(), name="watchlist-detail-cbv-try1"),
    path('watchlist-cbv-try2/', views.WatchlistCBView2.as_view(), name="watchlist-cbv-try2"),
    
    #StreamPlatform urls
    path('streamplatform-cbv-try1/', views.StreamPlatformDetailView1.as_view(), name="streamplatform-cbv-try1"),
    path('streamplatform-cbv-try2/', views.StreamPlatformListView2.as_view(), name="streamplatform-cbv-try2"),
    path('streamplatform-detail-cbv-try1/<int:pk>/', views.StreamPlatformDetailView1.as_view(), name="streamplatform-detail-cbv-try1"),
    path('streamplatform-detail-cbv-try2/<int:pk>/', views.StreamPlatformDetailView2.as_view(), name="streamplatform-detail-cbv-try2"),
    
    #Review urls
    path('reviewlist-cbv-try1/', views.ReviewlistCBView1.as_view(), name="reviewlist-cbv-try1"),
    
    
    
    
    
    
    
]
