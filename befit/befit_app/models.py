from django.db import models

class User(models.Model):
    name = models.CharField(blank=False, max_length=15)
    email = models.EmailField(blank=False, primary_key=True)
    
    def __str__(self):
            return self.name
    


class Article(models.Model):
    title = models.CharField(blank=False, max_length=200)
    content = models.TextField(blank=False)
    issued = models.DateTimeField()
    image = models.ImageField(upload_to='uploads', blank=True,null=True)
    
    def __str__(self):
        return self.title

class Food(models.Model):
    name = models.CharField(max_length=200 ,null=False)
    quantity = models.PositiveIntegerField(null=False, default=0)
    calorie = models.FloatField(null=False, default=0)
   
    
    def __str__(self):
        return self.name