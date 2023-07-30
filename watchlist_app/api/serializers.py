from rest_framework import serializers
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api import fields

User = get_user_model()

class StreamPlatformSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    about = serializers.CharField(max_length=150)
    website = serializers.URLField(max_length=100)

class WatchlistSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    storyline = serializers.CharField(max_length=200)
    active = serializers.BooleanField()
    # platform = StreamPlatformSerializer()
    # platform = serializers.StringRelatedField()
    # platform = serializers.HyperlinkedRelatedField(view_name='streamplatform-detail-cbv-try1', read_only=True)
    # platform = serializers.HyperlinkedIdentityField(view_name='streamplatform-detail-cbv-try1', read_only=True)
    platform = serializers.SlugRelatedField(slug_field="name", queryset=StreamPlatform.objects.all())
    imdb_rating = serializers.FloatField(default=0)
    created = serializers.DateTimeField()
    episodes = serializers.IntegerField(default=0)
    category = serializers.CharField(max_length=30) 
    
    def create(self, validated_data):
        return WatchList.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Watchlist` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.storyline = validated_data.get('storyline', instance.storyline)
        instance.active = validated_data.get('active', instance.active)
        instance.platform = validated_data.get('platform', instance.platform)
        instance.imdb_rating = validated_data.get('imdb_rating', instance.imdb_rating)
        instance.created = validated_data.get('created', instance.created)
        instance.episodes = validated_data.get('episodes', instance.episodes)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
    
    def validate_title(self, value):
        if "@" in value:
            serializers.ValidationError("Invalid Title")
        return value
    
    def validate_storyline(self, value):
        if "@" in value:
            serializers.ValidationError("Invalid Storyline")
        return value
    
    def validate_category(self, value):
        if value not in ["MOVIE", "SERIES"]:
            serializers.ValidationError("Not a valid category")
        return value
    
    def validate_platform(self, value):
        return value
    
    def validate(self, data):
        title = data.get("title", None)
        storyline = data.get("storyline", None)
        if (title and storyline) and (len(title) > len(storyline)):
            raise serializers.ValidationError("Length of title is bigger than storyline")
        return super().validate(data)
    
class ReviewSerializer(serializers.Serializer):
    review_user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    rating = serializers.IntegerField()
    description = serializers.CharField(max_length=200)
    watchlist = WatchlistSerializer()
    active = serializers.BooleanField()
    created = serializers.DateTimeField()
    update = serializers.DateTimeField()
    
#############################ModelSerializer#########################

class WatchListModelSerializer(serializers.ModelSerializer):
    full_title = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    # created = CustomDateTimeSerializerField()    
    # serializer_field_mapping = {
    #     models.DateTimeField: CustomDateTimeField,
    # }
    serializer_related_field = fields.CustomPrimaryKeyRelatedField
    # platform = serializers.HyperlinkedRelatedField(view_name='streamplatform-detail-cbv-try2', read_only=True)
    # serializer_url_field = fields.CustomHyperlinkedRelatedField
    serializer_choice_field = fields.CustomChoiceField
    
    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ["title", "storyline", "platform"]
        read_only_fields = ['full_title']
        extra_kwargs = {
            'imdb_rating': {'validators':[MinValueValidator(1.0), MaxValueValidator(5.0)]}
        }
        
        
    def get_full_title(self, obj):
        return obj.full_title
        
    def validate_title(self, value):
        if "@" in value:
            serializers.ValidationError("Invalid Title")
        return value
    
    def validate_storyline(self, value):
        if "@" in value:
            serializers.ValidationError("Invalid Storyline")
        return value
    
    def validate_category(self, value):
        if value not in ["MOVIE", "SERIES"]:
            serializers.ValidationError("Not a valid category")
        return value
    
    def validate_platform(self, value):
        return value
    
    def validate(self, data):
        title = data.get("title", None)
        storyline = data.get("storyline", None)
        if (title and storyline) and (len(title) > len(storyline)):
            raise serializers.ValidationError("Length of title is bigger than storyline")
        return super().validate(data)
    
class StreamPlatformModelSerializer(serializers.ModelSerializer):
    watchlist = WatchListModelSerializer(many=True, read_only=True)
    serializer_url_field = fields.CustomHyperlinkedRelatedField

    class Meta:
        model = StreamPlatform
        fields = "__all__"
        depth = 1
        extra_kwargs = {
            'about':{'allow_null':True, 'default':""},
            'website':{'required': False}
        }

class ReviewModelSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"
        
#############################HyperlinkedModelSerializer#########################

class WatchListHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    full_title = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = WatchList
        fields = "__all__"
        # exclude = ["platform"]
        # fields = ["title", "storyline", "platform"]
        read_only_fields = ['full_title']
        extra_kwargs = {
            'imdb_rating': {'validators':[MinValueValidator(1.0), MaxValueValidator(5.0)]},
            'platform': {'view_name':'streamplatform-detail-cbv-try3'},
            'url': {'view_name': 'watchlist-detail-cbv-try3', 'lookup_field': 'pk'},         
        }
        
        
    def get_full_title(self, obj):
        return obj.full_title
        
    def validate_title(self, value):
        if "@" in value:
            serializers.ValidationError("Invalid Title")
        return value
    
    def validate_storyline(self, value):
        if "@" in value:
            serializers.ValidationError("Invalid Storyline")
        return value
    
    def validate_category(self, value):
        if value not in ["MOVIE", "SERIES"]:
            serializers.ValidationError("Not a valid category")
        return value
    
    def validate_platform(self, value):
        return value
    
    def validate(self, data):
        title = data.get("title", None)
        storyline = data.get("storyline", None)
        if (title and storyline) and (len(title) > len(storyline)):
            raise serializers.ValidationError("Length of title is bigger than storyline")
        return super().validate(data)
    
class StreamPlatformHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListHyperlinkedModelSerializer(many=True, read_only=True)
    serializer_url_field = fields.CustomHyperlinkedRelatedField

    class Meta:
        model = StreamPlatform
        fields = "__all__"
        depth = 1
        extra_kwargs = {
            'about':{'allow_null':True, 'default':""},
            'website':{'required': False},
            'url':{'view_name':'streamplatform-detail-cbv-try3', 'lookup_field':'name'}            
        }

