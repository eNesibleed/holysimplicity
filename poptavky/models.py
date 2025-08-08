from django.db import models

class Poptavka(models.Model):
    email = models.EmailField()
    zprava = models.TextField()
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Poptávka od {self.email} ({self.datum.strftime('%d.%m.%Y %H:%M')})"
