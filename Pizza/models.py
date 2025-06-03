from django.db import models

class Pije(models.Model):
    emri = models.CharField(max_length=100)
    pershkrimi = models.TextField(blank=True)
    cmimi = models.DecimalField(max_digits=5, decimal_places=2)
    foto = models.ImageField(upload_to='pijet/', blank=True, null=True)

    def __str__(self):
        return self.emri


class Pizza(models.Model):
    emri = models.CharField(max_length=100)
    pershkrimi = models.TextField()
    cmimi = models.DecimalField(max_digits=5, decimal_places=2)
    foto = models.ImageField(upload_to='pizza_foto/', null=True, blank=True)

    def __str__(self):
        return self.emri


class Porosi(models.Model):
    emri = models.CharField(max_length=100)
    numri = models.CharField(max_length=15)  
    adresa = models.TextField()
    pijet = models.ManyToManyField(Pije, blank=True)
    pizzat = models.ManyToManyField(Pizza, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Porosi nga {self.emri} më {self.data.strftime('%Y-%m-%d %H:%M')}"


class Kontakt(models.Model):
    emri = models.CharField(max_length=100)
    email = models.EmailField()
    mesazhi = models.TextField()
    data_dergimit = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.emri} - {self.email}"
