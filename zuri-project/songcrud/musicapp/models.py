from django.db import models
from django.utils import timezone

class Artiste(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} is a great Artiste who is {self.age} years of age"


class Song(models.Model):
    title = models.CharField(max_length= 120)
    date_released = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.artiste_id.first_name} released a song with title {self.title} on {self.date_released} with a superb amount of {self.likes} likes"


class Lyric(models.Model):
    content = models.TextField(max_length= 50)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.content.title}\n{self.content}"