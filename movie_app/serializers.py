from .models import Director, Movie, Review
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie stars'.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'title description duration director reviews'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    filtered_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title description duration director filtered_reviews rating'.split()

    def get_filtered_reviews(self, movie):
        reviews = Review.objects.filter(movie=movie, stars__gt=3)
        return ReviewSerializer(reviews, many=True).data


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'title reviews rating'.split()



class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie stars'.split()



class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100)

    def validate_name(self, name):
        directors = Director.objects.filter(name=name)
        if directors.count() > 0:
            raise ValidationError('Product must be unique!')
        return name



class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3)
    description = serializers.CharField(required=False)
    duration = serializers.CharField()
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director does not exists!')
        return director_id

    def validate_title(self, title):
        movies = Movie.objects.filter(title=title)
        if movies.count() > 0:
            raise ValidationError('Movie must be unique!')
        return title



class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_review_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Movie does not exists!')
        return movie_id