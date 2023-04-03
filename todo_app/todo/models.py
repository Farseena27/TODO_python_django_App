from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Tasks(models.Model):
    title= models.CharField(max_length=200)
    description = models.TextField(default=None)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

