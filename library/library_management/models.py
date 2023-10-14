from django.db import models

# Create your models here.
# 1st model
class Library(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=255, null=False)
    established_date = models.DateField(null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'

# 2nd model
class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=100, null=False)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# 3rd model
class Member(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    membership_date = models.DateField(null=False)
    email = models.EmailField(unique=True)
    # borrowed_books = models.ManyToManyField(Book)

    def __str__(self):
        return (f"{self.first_name}{self.last_name}")


class BorrowedBook(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField

    def __str__(self):
        return (f"{self.member.first_name} borrowed {self.book.title}")




