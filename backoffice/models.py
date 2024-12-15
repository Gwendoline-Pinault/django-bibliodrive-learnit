from django.db import models


class Author(models.Model):
    au_id = models.AutoField(primary_key=True, null=False)
    author = models.CharField(max_length=50)
    year_born = models.SmallIntegerField()

    def __str__(self):
        return self.author


class Publisher(models.Model):
    pubid = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=50)
    compagny_name = models.CharField(max_length=255)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=10)
    zip = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    comments = models.TextField()

    def __str__(self):
        return self.name


class Title(models.Model):
    title_id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=255)
    year_published = models.SmallIntegerField()
    isbn = models.CharField(max_length=20)
    pubid = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    comments = models.TextField()
    authors = models.ManyToManyField(Author)
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='no-image')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True, null=False)
    reservation_date = models.DateField()
    return_date = models.DateField()
    # book_id = models.ForeignKey(Title, on_delete=models.CASCADE)
