from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Post(models.Model):
	title = models.CharField(max_length=250)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	pub_date = models.DateField('date published')
	header_image = models.ImageField(null=True, blank=True, upload_to="images/")

	def __str__(self):
		return self.title + ' | ' + str(self.author)

class Comment(models.Model):
	post = 	models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)

