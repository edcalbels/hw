from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100, unique=True)

    @property
    def movies_count(self):
        total_movie = self.movies.all().count()
        if total_movie == 0:
            return 0
        return total_movie

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    duration = models.TextField(max_length=10)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    

    @property
    def rating(self):
        total_amount = self.reviews.all().count()
        if total_amount == 0:
            return 0
        sum_ = 0
        for i in self.reviews.all():
            sum_ += i.stars
        return sum_ / total_amount

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(max_length=1000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=1)

    def __str__(self):
        return self.text