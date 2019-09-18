from django.db import models


class Article(models.Model):
	news_title = models.CharField(max_length=50)
	content = models.TextField()
	author = models.TextField(max_length=20)

	def __str__(self):
		return self.news_title[:50]


# Create your models here.
