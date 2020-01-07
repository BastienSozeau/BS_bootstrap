from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    text_content = models.CharField(max_length=2000)
    image = models.FilePathField(path="/img")
