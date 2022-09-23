from django.conf import settings
from django.db import models
from django.utils import timezone

# create the post model for blog
# Post inherite from modles.Model
class Post(models.Model):
	# models.ForeignKey – link to another model
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	# text with a limited number of characters
	title = models.CharField(max_length=200)
	# long text without limit
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()


	# like the java toString method, provide how to print this object in string
	def __str__(self):
		return self.title
