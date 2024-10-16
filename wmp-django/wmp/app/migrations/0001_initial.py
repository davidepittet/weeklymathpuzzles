# Generated by Django 5.1.1 on 2024-10-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Archive",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("yearWeak", models.CharField(db_index=True, max_length=6)),
                ("text", models.TextField()),
                ("ans1", models.IntegerField()),
                ("ans2", models.IntegerField()),
                ("ans3", models.IntegerField()),
                ("ans4", models.IntegerField()),
                ("ans5", models.IntegerField()),
                ("correctAnswer", models.IntegerField()),
            ],
        ),
    ]
