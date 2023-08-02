from django.urls import path, include
from watchlist_app.api import views

urlpatterns = [
    # Using Basic Serializer for the views
    path('watchlist-cbv-try1/', views.WatchlistCBView1.as_view(), name="watchlist-cbv-try1"),
    path('watchlist-detail-cbv-try1/<int:pk>/', views.WatchlistDetailCBView1.as_view(), name="watchlist-detail-cbv-try1"),
    path('streamplatform-cbv-try1/', views.StreamPlatformDetailView1.as_view(), name="streamplatform-cbv-try1"),
    path('streamplatform-detail-cbv-try1/<int:pk>/', views.StreamPlatformDetailView1.as_view(), name="streamplatform-detail-cbv-try1"),
    
    # Using ModelSerializer for the views
    path('watchlist-cbv-try2/', views.WatchlistCBView2.as_view(), name="watchlist-cbv-try2"),
    path('streamplatform-cbv-try2/', views.StreamPlatformListView2.as_view(), name="streamplatform-cbv-try2"),
    path('streamplatform-detail-cbv-try2/<int:pk>/', views.StreamPlatformDetailView2.as_view(), name="streamplatform-detail-cbv-try2"),
    
    # Using HyperlinkedModelSerializer for the views
    path('watchlist-cbv-try3/', views.WatchlistCBView3.as_view(), name="watchlist-cbv-try3"),
    path('watchlist-detail-cbv-try3/<int:pk>/', views.WatchlistDetailCBView3.as_view(), name="watchlist-detail-cbv-try3"),
    path('watchlist-detail-cbv-try3/<int:pk>/', views.WatchlistDetailCBView3.as_view(), name="watchlist-detail-cbv-try3"),
    path('streamplatform-detail-cbv-try3/<int:pk>/', views.StreamPlatformDetailView3.as_view(), name="streamplatform-detail-cbv-try3"),
    
    # Using ListSerializer for the views
    path('watchlist-cbv-try4/', views.WatchlistCBView4.as_view(), name="watchlist-cbv-try4"),
    
    # Using BaseSerializer for the views
    path('watchlist-cbv-try5/', views.WatchlistCBView5.as_view(), name="watchlist-cbv-try5"),
    
    
    
    
    
    
    
    #Review urls
    path('reviewlist-cbv-try1/', views.ReviewlistCBView1.as_view(), name="reviewlist-cbv-try1"),
    
    
    
    
    
    
    
]
