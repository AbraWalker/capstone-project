from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rating(models.IntegerChoices):
    ONE_STAR = 1, "One Star"
    TWO_STAR = 2, "Two Stars"
    THREE_STAR = 3, "Three Stars"
    FOUR_STAR = 4, "Four Stars"
    FIVE_STAR = 5, "Five Stars"

Completed =  ((0, "Incomplete"), (1, "Complete"))

class Post(models.Model):
    #temporary game identifier
    game_title = models.CharField(default='Game Title Here', max_length=200)
    slug = models.SlugField(default=0, max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    content = models.CharField(max_length=250)
    overall_rating = models.IntegerField(default=Rating.ONE_STAR, choices=Rating.choices)
    difficulty_rating = models.IntegerField(default=Rating.ONE_STAR, choices=Rating.choices)
    value_rating = models.IntegerField(default=Rating.ONE_STAR, choices=Rating.choices)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["overall_rating"]


class Guide(models.Model):
    game_title = models.CharField(default="Game Title Here", max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="guide"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    completed = models.IntegerField(choices=Completed, default=0)
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title} - Guide by {self.author} ({self.completed})"


class Opinions(models.IntegerChoices):
    AGREE = 0, "Good Take"
    DISAGREE = 1, "Bad Take"

class UserVotes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="opinions")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    user_rating = models.IntegerField(default=Opinions.AGREE, choices=Opinions.choices)
