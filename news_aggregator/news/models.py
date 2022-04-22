from django.db import models

# Create your models here.
class Query(models.Model):
    query = models.TextField()
    date_of_query = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Queries"
    
    def __str__(self):
        return self.query

class Article(models.Model):
    headline = models.TextField()
    link = models.TextField()
    source = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Articles"
        
    def __str__(self):
        return str(self.id) + ": " + self.headline
    
class User(models.Model):
    user = models.CharField(max_length=200, primary_key=True)
    articles = models.ManyToManyField(Article, through='Saved')
    
    class Meta:
        verbose_name_plural = "Users"
    
    def __str__(self):
        return self.user
    
class Saved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    favourite = models.BooleanField(default=False)
    date_of_fav = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Saved Articles"
    
    def __str__(self):
        return self.user.user + ': ' + str(self.article.id) + ': ' + self.article.headline
