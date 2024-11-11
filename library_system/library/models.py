from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,related_name="books",on_delete=models.CASCADE)
    published_date = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=100)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title


