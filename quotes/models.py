from django.db import models
from django.utils import timezone


class Quote(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  attribution = models.CharField(max_length=200)
  quote_text = models.TextField()
  quote_source = models.CharField(
    max_length=300,
    default="Source Unknown",
    help_text="Who said or wrote this quotation?"
  )
  created_date = models.DateTimeField(
    default=timezone.now)
  published_date = models.DateTimeField(
    blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.attribution



