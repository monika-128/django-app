from django.db import models
import uuid
# Create your models here.
class BaseClass(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(BaseClass):
    fullname = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    subject = models.CharField(max_length=255, blank=False, null=False)
    message = models.TextField()

class Team(BaseClass):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']   # automatically order by this field

    def __str__(self):
        return self.name
    
class Category(BaseClass):
    name = models.CharField(max_length=255, blank=False, null=False)
    

class Blog(BaseClass):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to="blogs/")
    title = models.CharField(max_length=255, blank=False, null=False)
    content  = models.TextField()
    author = models.CharField(max_length=255, blank=False, null=False)
    