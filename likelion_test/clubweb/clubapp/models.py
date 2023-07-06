from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    numofpeople = models.IntegerField()

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    club = models.ForeignKey(Club, on_delete = models.CASCADE)
    comment = models.CharField(max_length = 100)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.comment