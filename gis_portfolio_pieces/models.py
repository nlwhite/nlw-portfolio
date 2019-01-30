from django.db import models

# Create your models here.


class PortItem(models.Model):

    title = models.CharField(max_length=40)
    summary = models.CharField(max_length=120)
    intro_text = models.TextField(blank=True, null=True, max_length=3000)
    full_text = models.TextField(blank=True, null=True)
    image_thumb = models.ImageField(upload_to='images/%Y/%m/')
    date_created = models.CharField(blank=True, null=True, max_length=18)
    weight = models.IntegerField()

    def __str__(self):
        return self.title

class PortItemPiece(models.Model):
    title = models.CharField(blank=True, null=True, max_length=40)
    summary = models.TextField(blank=True, null=True)

    image_med = models.ImageField(upload_to='images/%Y/%m/')
    file_to_download = models.FileField(blank=True, null=True, upload_to='images/%Y/%m/')

    file_format = models.CharField(blank=True, null=True, max_length=20)
    piece_print_size = models.CharField(blank=True, null=True, max_length=20)
    piece_file_size = models.CharField(blank=True, null=True, max_length=20)

    external_link = models.URLField(blank=True, null=True)

    parent_piece = models.ForeignKey(PortItem, related_name='items', on_delete=models.CASCADE)
    weight = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
