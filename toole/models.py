from django.db import models
from django.utils import timezone

class Produkt(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.FileField(null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Partner(models.Model):
	title = models.CharField(max_length=200)
	link = models.TextField()
	image = models.FileField(null=True, blank=True)

	def publish(self):
		self.save()

	def __str__(self):
		return self.title

class Kariera(models.Model):
	stanowisko = models.CharField(max_length=200)
	plik = models.FileField(upload_to='')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def publish(self):
		self.save()

	def __str__(self):
		return self.stanowisko