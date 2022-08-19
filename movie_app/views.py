from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Director, Movie, Review
from rest_framework import status
from .serializers import (
    DirectorSerializer, 
    MovieSerializer, 
    ReviewSerializer, 
    MovieReviewSerializer, 
    MovieDetailSerializer, 
    DirectorDetailSerializer,
    ReviewDetailSerializer,
    DirectorValidateSerializer,
    MovieValidateSerializer,
    ReviewValidateSerializer
)
# from rest_framework.generics import (
#     ListAPIView,
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView
# )

from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet



@api_view(['GET', 'POST'])
def directors_views(request):
    print(request.user)
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'errors': serializer.errors})
        name = serializer.validated_data.get('name')
        Director.objects.create(
            name=name
        )
        serializer.save()
    return Response(data=request.data)

class DirectorAPIViewSet(ModelViewSet):
    """Category API"""
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination


@api_view(['GET', 'POST'])
def movies_views(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'errors': serializer.errors})
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )
    return Response(data=MovieSerializer(movie).data)


class MovieAPIViewSet(ModelViewSet):
    """Category API"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination

@api_view(['GET', "POST"])
def reviews_views(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'errors': serializer.errors})
        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        stars = serializer.validated_data.get('stars')
        Review.objects.create(
            text=text,
            movie_id=movie_id,
            stars=stars
        )
    return Response(data=request.data)

class ReviewAPIViewSet(ModelViewSet):
    """Category API"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination

@api_view(['GET'])
def movie_reviews(request):
    movies = Movie.objects.all()
    data = MovieReviewSerializer(movies, many=True).data
    return Response(data=request.data)

class MovieReviewAPIViewSet(ModelViewSet):
    """Category API"""
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer
    pagination_class = PageNumberPagination


@api_view(['GET', 'PUT', 'DELETE'])
def director_item_views(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorDetailSerializer(directors).data
        return Response(data=data)
    elif request.method == 'DELETE':
        directors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = DirectorValidateSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data = {'errors': serializer.errors})
        name = request.data.get('name')
        directors.name = name
        directors.save()
        return Response(data=DirectorSerializer(directors).data)



@api_view(['GET', 'PUT', 'DELETE'])
def movie_item_views(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieDetailSerializer(movies).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'errors': serializer.errors})
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movies.title = title
        movies.description = description
        movies.duration = duration
        movies.director_id = director_id
        movies.save()
        return Response(data=MovieSerializer(movies).data)




@api_view(['GET', 'PUT', 'DELETE'])
def review_item_views(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewDetailSerializer(reviews).data
        return Response(data=data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'errors': serializer.errors})
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        reviews.text = text
        reviews.movie_id = movie_id
        reviews.stars = stars
        reviews.save()
        return Response(data=ReviewSerializer(reviews).data)