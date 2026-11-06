from django.db import models

# Create your models here.

#movie directors details here
class Director(models.Model):
    name=models.CharField(max_length=250)
    
    def __str__(self):
            return self.name
    
#Actors details table class here
class Actor(models.Model):
    name=models.CharField(max_length=250)
    
    def __str__(self):
                return self.name

#censor info's for movie's
class CensorInfo(models.Model):
    rating=models.CharField(max_length=10)
    certified_by=models.CharField(max_length=200,null=True)
    
    def __str__(self):
                    return self.rating

#movie info tables for movie details
class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    summary=models.TextField()
    poster = models.ImageField(upload_to="images/", blank=True, null=True)
    censor_details=models.OneToOneField(CensorInfo,null=True,
                                        on_delete=models.SET_NULL, 
                                        related_name='movie')
    
    directed_by=models.ForeignKey(Director, null=True,
                                  on_delete=models.CASCADE,
                                  related_name='directed_movie')
    
    actors=models.ManyToManyField(Actor, related_name='acted_movies')
    
    def __str__(self):
        return self.title
    