from django.db import models 

# Create your models here.

#Author

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.author_name}"
    
#Category
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.category_name}"

#Book
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True) 
    image = models.ImageField(upload_to='books/')
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True, blank=True)
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
      return f"{self.book_id} - {self.title}"
    
    # contactt
class Contact(models.Model):
    contact_name = models.CharField(max_length=60, null=True, blank=True)
    contact_surname = models.CharField(max_length=60, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_comment = models.TextField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return f"{self.contact_name} - {self.contact_surname}"
# Subscriber
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email