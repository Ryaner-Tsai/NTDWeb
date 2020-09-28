from django.db import models


class DesignProject(models.Model):
    Title = models.CharField(max_length=255)
    Owner = models.CharField(max_length=255)
    ArchDesign = models.CharField(max_length=255)
    StructureType = models.CharField(max_length=255)
    Story = models.CharField(max_length=255)
    Area = models.CharField(max_length=255)
    Service = models.CharField(max_length=225)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Title