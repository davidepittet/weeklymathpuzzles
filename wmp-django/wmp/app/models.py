from django.db import models

# Create your models here.
class Archive(models.Model):
    # AnnoSettimana, Testo, Risposta 1, Risposta 2, ..., Risposta 5, Numero della risposta corretta
    yearWeak = models.CharField(max_length=6, db_index=True)
    text = models.TextField()

    ans1 = models.TextField()
    ans2 = models.TextField()
    ans3 = models.TextField()
    ans4 = models.TextField()
    ans5 = models.TextField()

    correctAnswer = models.IntegerField()

    def __str__(self):
        return f"\nID: {self.id} \nyearWeek: {self.yearWeak}"