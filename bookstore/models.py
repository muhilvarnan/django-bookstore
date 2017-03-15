from __future__ import unicode_literals
import uuid
from django.db import models
from django.db.models import Count

# Create your models here.
class Books(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Authors',related_name='authorname')
    publisher = models.ForeignKey('Publishers',related_name='publishername')
    retail_price = models.FloatField()

    def __str__(self):
      return self.title

class Authors(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
      return self.name
    
class Publishers(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
      return self.name

class Customers(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
      return self.name

class Orders(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    customer = models.ForeignKey('Customers')
    order_date = models.DateField(auto_now_add=True)
    book = models.ManyToManyField('Books')


def get_top_selling_books():
  """
  get top selling books
  """
  try:
    bookData = Orders.objects.values('book').annotate(count=Count('book')).order_by('-count')[:10]
    result = []
    for book in bookData:
      if book['book']:
        result.append(Books.objects.get(pk=book['book'].hex).title)
    return result
  except Exception, e:
    print e
    return []

def get_top_authors():
  """
  get top selling books
  """
  try:
    bookData = Orders.objects.values('book').annotate(count=Count('book')).order_by('-count')
    print bookData
    result = []
    limit = 1
    for book in bookData:
      if book['book']:
        if(limit>=10):
          break
        print book['book'].hex
        if Books.objects.get(pk=book['book'].hex).author.name not in result:
          result.append(Books.objects.get(pk=book['book'].hex).author.name)
          limit = limit + 1
    return result 
  except Exception, e:
    print e
    return []