from django.db import models
from django.utils import timezone

# each class is going to be a tables in a database
class Post(models.Model): 
# now the atributes is going to be a differnt filed in the database
     title = models.CharField(max_length=100)
     content = models.TextField()
     date_posted = models.DateTimeField(default=timezone.now)
     