from django.contrib.auth.models import User
from django.db import models
# Django administration ADMIN
class Category(models.Model):
	name = models.CharField(max_length=255)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = 'Marci auto'

	def __str__(self):
		return self.name 

class Articol(models.Model):
	category = models.ForeignKey(Category, related_name='articol', on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	price = models.FloatField()
	image = models.ImageField(upload_to='articol_images', blank=True, null=True)
	is_sold = models.BooleanField(default=False)
	created_by = models.ForeignKey(User, related_name='articol', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	# sa afiseze modelele de masini in Articol
	def __str__(self):
		return self.name 
