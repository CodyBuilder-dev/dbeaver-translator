from django.db import models

# Create your models here.
class File(models.Model):
    package_name = models.CharField(max_length = 200)
    file_name = models.CharField(max_length = 200)

class Property(models.Model):
    name = models.CharField(max_length=200)
    value_en = models.CharField(max_length=200)
    value_ko = models.CharField(max_length=200)
    value_ko_utf = models.CharField(max_length=200)
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    def __str__(self):
        return self.property_name + '=' + self.property_en

class UploadFileModel(models.Model):
    package_name = models.CharField(default='org.jkiss.dbeaver',max_length=200)
    file_name = models.CharField(default='bundle.properties',max_length=200)
    file = models.FileField(null=True)
