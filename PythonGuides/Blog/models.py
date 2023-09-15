from django.db import models

class Blog(models.Model):
    BlogId = models.BigIntegerField()
    Title = models.CharField(max_length=200)
    Content = models.CharField(max_length=300)
    Image = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=100)


    class Meta:
        db_table = 'Blog'