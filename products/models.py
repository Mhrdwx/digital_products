from django.db import models

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey("self" , verbose_name="parent", on_delete=models.CASCADE , blank=True, null=True)
    title = models.CharField("title",max_length=50)
    description = models.TextField("description",blank=True)
    avatar = models.ImageField(blank=True,upload_to="categories")
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "categories" #table in database
        verbose_name = "Category" #admin panel
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField("title" , max_length=50)
    description = models.TextField("description" , blank=True)
    avatar =  models.ImageField("avatar" , blank=True , upload_to="products/")
    is_enable = models.BooleanField(default=True)
    categories = models.ManyToManyField("Category" , verbose_name="categories" , blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products"
        verbose_name = "Product" #For admin panel
        verbose_name_plural = "Products"
    def __str__(self):
        return self.title


class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPES = (
        (FILE_AUDIO, "Audio File"),
        (FILE_VIDEO, "Video File"),
        (FILE_PDF, "PDF file"),
    )
    product = models.ForeignKey("Product" , verbose_name="product" ,related_name="files" ,on_delete=models.CASCADE)
    title = models.CharField("title" , max_length=50)
    file_type = models.IntegerField("file type",choices=FILE_TYPES , default=FILE_AUDIO ,)
    file = models.FileField("file" , blank=True , upload_to="files/%Y/%m/%d/")
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "files"
        verbose_name = "File"
        verbose_name_plural = "Files"

    def __str__(self):
        return self.title
