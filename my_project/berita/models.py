from django.db import models

class Berita(models.Model):
    kategori = models.CharField(max_length=200)
    judul = models.CharField(max_length=200)
    isi_berita = models.TextField()

class Kategori(models.Model):
    nama_Kategori = models.CharField(max_length=200)

    #def __str__(self):
        #return f"{self.nama_Kategori}"





    #def __str__(self):
        #return f"{self.judul}"

    