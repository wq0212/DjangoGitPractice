from django.db import models

# Create your models here.
class MainBoard(models.Model):
    title = models.CharField('TITLE',max_length = 50)
    contents = models.TextField('CONTENTS')
    cdate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title