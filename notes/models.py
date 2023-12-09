from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    color=models.CharField(max_length=20,blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title