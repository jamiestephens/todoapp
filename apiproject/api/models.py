from django.db import models

# Create your models here.class Task(models.Model):
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True,null=True)
    estimated_time = models.PositiveIntegerField(default=1)
    objects = models.Manager()
    
    def __str__(self):
        return self.title