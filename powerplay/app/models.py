from django.db import models


class System(models.TextChoices):
    GAMEBOY = "GB"
    GAMEBOY_COLOR = "GBC"


class Game(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    music_file = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    publisher = models.CharField(max_length=255)
    studio = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    review_score = models.PositiveSmallIntegerField()
    release_date = models.DateField()
    box_art_url = models.URLField()
    box_art = models.BinaryField()
    system = models.CharField(
        max_length=3,
        choices=System.choices,
        default=System.GAMEBOY,
    )


class Screenshot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    image = models.BinaryField()
