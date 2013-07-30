from django.db import models
import datetime
# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.CharField(max_length=10000)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	user = models.CharField(max_length=20, default="NULL")
	article = models.ForeignKey(Article)
	content = models.CharField(max_length=1000)
	pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

	def __unicode__(self):
		return self.id