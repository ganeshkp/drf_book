from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from django.http import Http404
from watchlist_app.models import WatchList, Review, StreamPlatform
from . import serializers

################################Class Based Views##############################

#=============Views Using Basic Serializer=================
class WatchlistCBView1(APIView):
    """
    View to list all Movies in the system.
    """
    def get(self, request, format=None):
        """
        Return a list of all watchlist.
        """
        watchlist = WatchList.objects.all()
        serializer = serializers.WatchlistSerializer(watchlist, many = True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        Create a new watchlist.
        """
        serializer = serializers.WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class WatchlistDetailCBView1(APIView):
    """
    View in detail individual Watchlist in the system.
    """
    def get(self, request, pk, format=None):
        try:
            watchlist = WatchList.objects.get(pk=pk)
            serializer = serializers.WatchlistSerializer(watchlist)
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            raise Http404
        
    def put(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
            serializer = serializers.WatchlistSerializer(watchlist, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WatchList.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
            serializer = serializers.WatchlistSerializer(watchlist, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            raise Http404
        
    def delete(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
            watchlist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as err:
            raise Http404
        
class StreamPlatformDetailView1(APIView):
    """
    Stream Platform Detail View
    """
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.StreamPlatformSerializer(platform)
        return Response(serializer.data)
        
class ReviewlistCBView1(APIView):
    """
    View to list all Reviews in the system.
    """
    def get(self, request, format=None):
        """
        Return a list of all watchlist.
        """
        reviews = Review.objects.all()
        serializer = serializers.ReviewSerializer(reviews, many = True)
        return Response(serializer.data)
    
    
#=============Views Using ModelSerializer=================
class WatchlistCBView2(APIView):
    """
    View to list all Movies in the system.
    """
    def get(self, request, format=None):
        """
        Return a list of all watchlist.
        """
        watchlist = WatchList.objects.all()
        serializer = serializers.WatchListModelSerializer(watchlist, many = True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        Create a new watchlist.
        """
        serializer = serializers.WatchListModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatformListView2(APIView):
    """
    Stream Platform List View
    """
    
    def get(self, request, format=None):
        """
        Return a list of all watchlist.
        """
        watchlist = StreamPlatform.objects.all()
        serializer = serializers.StreamPlatformModelSerializer(watchlist, many = True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        Create a new watchlist.
        """
        serializer = serializers.StreamPlatformModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailView2(APIView):
    """
    Stream Platform Detail View
    """
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.StreamPlatformModelSerializer(platform)
        return Response(serializer.data)
        
class ReviewlistCBView2(APIView):
    """
    View to list all Reviews in the system.
    """
    def get(self, request, format=None):
        """
        Return a list of all watchlist.
        """
        reviews = Review.objects.all()
        serializer = serializers.ReviewModelSerializer(reviews, many = True)
        return Response(serializer.data)
        
#=============Views Using HyperLinkedModelSerializer=================
class WatchlistCBView3(APIView):
    """
    View to list all Movies in the system.
    """
    def get(self, request, format=None):
        """
        Return a list of all watchlist.
        """
        watchlist = WatchList.objects.all()
        serializer = serializers.WatchListHyperlinkedModelSerializer(watchlist, many = True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        Create a new watchlist.
        """
        serializer = serializers.WatchListHyperlinkedModelSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WatchlistDetailCBView3(APIView):
    """
    View in detail individual Watchlist in the system.
    """
    def get(self, request, pk, format=None):
        try:
            watchlist = WatchList.objects.get(pk=pk)
            serializer = serializers.WatchListHyperlinkedModelSerializer(watchlist, context={'request': request})
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            raise Http404
        

class StreamPlatformDetailView3(APIView):
    """
    Stream Platform Detail View
    """
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.StreamPlatformHyperlinkedModelSerializer(platform, context={'request': request})
        return Response(serializer.data)
  
#=============Views Using ListModelSerializer=================
class WatchlistCBView4(APIView):
    """
    View to list all Movies in the system.
    """
    def get(self, request, format=None):
        """
        Return a list of all watchlist.
        """
        watchlist = WatchList.objects.all()
        serializer = serializers.WatchlistDemoListSerializer(watchlist, many = True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        Create a new watchlist.
        """
        serializer = serializers.WatchlistDemoListSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, format=None):
        serializer = serializers.WatchlistDemoListSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        # Perform the bulk update
        serializer.save()

        return Response(serializer.data)


#=============Views Using BaseSerializer=================
class WatchlistCBView5(APIView):
    """
    View to list all Movies in the system.
    """
    def get(self, request, format=None):
        """
        Return a list of all watchlist.
        """
        watchlist = WatchList.objects.all()
        serializer = serializers.WatchlistBaseSerializer(watchlist, many = True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        Create a new watchlist.
        """
        serializer = serializers.WatchlistBaseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#=============Views Using GenericAPIView=================
class WatchlistCBView6(generics.GenericAPIView):
    queryset = WatchList.objects.all()
    serializer_class = serializers.WatchListModelSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # Set the filter backends
    
    # Specify the fields that can be used for search and ordering
    search_fields = ['title','imdb_rating']
    ordering_fields = ['title', 'imdb_rating', 'created']
    
    def get_serializer_class(self):
        # Determine the serializer class based on the request method
        if self.request.method == 'POST':
            return serializers.WatchListModelSerializer
        elif self.request.method == 'GET':
            return serializers.WatchlistModelBasicSerializer
    
    def get(self, request, *args, **kwargs):
        """
        Return a list of all watchlist.
        """
        watchlist = queryset = self.filter_queryset(self.get_queryset())  # Apply search filter
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(watchlist, many=True, context={"request":request})
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        """
        Create a new watchlist.
        """
        serializer_class = self.get_serializer_class(data=request.data)
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class WatchlistDetailVBView6(generics.GenericAPIView):
    queryset = WatchList.objects.all()
    serializer_class = serializers.WatchListModelSerializer
    lookup_field = "title" # Set the lookup field to 'title' or any other field you prefer
    lookup_url_kwarg = 'title'
    




################################Function Based Views##############################
@api_view(['GET', 'POST'])
def WatchlistFunctionView(request):
    if request.method == 'GET':
        watchlist = WatchList.objects.all()
        serializer = serializers.WatchlistSerializer(watchlist, many=True)
        # Handle GET request
        data = {'message': 'This is a GET request'}
        return Response(serializer.data)
    elif request.method == 'POST':
        # Handle POST request
        data = {'message': 'This is a POST request'}
        return Response(data)
    
    