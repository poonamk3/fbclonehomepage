from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=200)
	image =models.ImageField(upload_to ='images/')
	author =models.ForeignKey(User,on_delete= models.CASCADE,null=True,blank=True)
	description=models.TextField()
	updated_at=models.DateTimeField(auto_now= True)
	created_at=models.DateTimeField(auto_now_add=True)
	likes=models.ManyToManyField(User,blank=True, related_name='likes')
	def likeuser(self):
		return ",".join(str(i) for i in self.likes.all())
	def likeusers(self):
		return self.likes.all().count()      
	
    