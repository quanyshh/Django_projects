from django.db import models
from django.forms import ModelForm
import os


def image_folder(instance, filename):
    filename = filename.split('.')[0]+ '/' +filename
    print(filename)
    return filename


class WorkSheet(models.Model):
    model_pic = models.ImageField(upload_to = image_folder, blank=True)


class UploadWorkSheetForm(ModelForm):
    class Meta:
        model = WorkSheet
        fields = '__all__'
