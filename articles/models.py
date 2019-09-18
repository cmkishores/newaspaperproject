from django.db import models


class Article(models.Model):
	news_title = models.CharField(max_length=50)
	content = models.textField()
	author = models.textField(max_length=20)

	def __str__(self):
		return self.title[:50]

	
# Create your models here.
