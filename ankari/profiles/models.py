from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .utils import get_random_code


class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="Nothing", max_length=300)
    email = models.EmailField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='avatar.jpg', upload_to='avatars/')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self) -> str:
        return f"{self.user.username} - {self.created.strftime('%d-%m-%Y')}"
    
    def get_friends(self):
        return self.friends.all()
    
    def get_friends_quantity(self):
        return self.friends.all().count()
    
    def get_post_quantity(self):
        return self.posts.all().count() # Потому что мы установили related_name в Post

    def get_all_authors_posts(self):
        return self.posts.all()
    
    def get_likes_given_quantity(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value == 'Like':
                total_liked += 1
        return total_liked
    
    def get_likes_received_quantity(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.liked.all().count()
        return total_liked
        
    
    def save(self, *args, **kwargs):
        ex = False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
            ex = Profile.objects.filter(slug=to_slug)
            while ex:
                to_slug = slugify(to_slug + " " + str(get_random_code))
                ex = Profile.objects.filter(slug=to_slug)
        else:
            to_slug = str(self.user)
        
        self.slug = to_slug
        super().save(*args, **kwargs)


STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self) -> str:
        return f"{self.sender} - {self.receiver} - {self.status}"