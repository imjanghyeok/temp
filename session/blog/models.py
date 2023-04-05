from django.db import models

# Create your models here.
class Blog(models.Model):
    category_list=(('d', 'diary'),('l','likelion'),('s','study'))
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    category = models.CharField(max_length=1, default='d', choices=category_list)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]