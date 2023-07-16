from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from watchlist_app.models import WatchList, Review, StreamPlatform
from .serializers import WatchlistSerializer, ReviewSerializer, StreamPlatformSerializer

################################Class Based Views##############################
class WatchlistCBView1(APIView):
    """
    View to list all Movies in the system.
    """
    def get(self, request, format=None):
        """
        Return a list of all watchlist.
        """
        watchlist = WatchList.objects.all()
        serializer = WatchlistSerializer(watchlist, many = True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        Create a new watchlist.
        """
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
class WatchlistDetailCBView1(APIView):
    """
    View to list all Movies in the system.
    """
    def get(self, request, pk, format=None):
        try:
            watchlist = WatchList.objects.get(pk=pk)
            serializer = WatchlistSerializer(watchlist)
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            raise Http404
        
    def put(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
            serializer = WatchlistSerializer(watchlist, data=request.data)
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
            serializer = WatchlistSerializer(watchlist, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            raise Http404
    


class ReviewlistCBView1(APIView):
    """
    View to list all Reviews in the system.
    """
    def get(self, request, format=None):
        """
        Return a list of all watchlist.
        """
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many = True)
        return Response(serializer.data)
    

class StreamPlatformDetailView1(APIView):
    """
    Stream Platform Detail View
    """
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    


################################Function Based Views##############################
@api_view(['GET', 'POST'])
def WatchlistFunctionView(request):
    if request.method == 'GET':
        watchlist = WatchList.objects.all()
        serializer = WatchlistSerializer(watchlist, many=True)
        # Handle GET request
        data = {'message': 'This is a GET request'}
        return Response(serializer.data)
    elif request.method == 'POST':
        # Handle POST request
        data = {'message': 'This is a POST request'}
        return Response(data)