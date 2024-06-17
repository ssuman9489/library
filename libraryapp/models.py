from django.db import models


class Bookdata(models.Model):
    id = models.IntegerField(primary_key=True)
    BookName = models.CharField(max_length=50)
    Description  = models.CharField(max_length=500)
    Author = models.CharField(max_length=50)
    Price = models.IntegerField()
    Category = models.CharField(max_length=50)
    Pages = models.IntegerField()
    Date_Of_Publish = models.DateField()
    Photo = models.ImageField(upload_to='book_photos/', blank=True, null=True)
    
    def __str__(self):
        return self.BookName
    
class Details(models.Model):
    id = models.IntegerField(primary_key=True)
    Fullname = models.CharField(max_length=300)
    Username = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    DOB = models.DateField()
    Gender = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    Aadhar = models.CharField(max_length=12)
    Phone = models.CharField(max_length=15)
    Profilepic = models.ImageField(upload_to='profile_pics/', blank=True)  
    
class contacts(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300) 
    email = models.EmailField() 
    phone = models.CharField(max_length=15) 
    message = models.CharField(max_length=50000)  
    
class IssuedBook(models.Model):
    id = models.IntegerField(primary_key=True)
    issuedate = models.DateField()
    returndate = models.DateField()