from django.core import validators, exceptions
from django.db import models


def validate_string_alphanumeric(value):
    for char in value:
        if not char.isalnum() and char != '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            validators.MinLengthValidator(MIN_USERNAME_LENGTH),
            validate_string_alphanumeric
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )


class Album(models.Model):
    MAX_ALBUM_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER_MUSIC = 'Other'

    MUSICS = [
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC)
    ]

    album_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        verbose_name='Album Name',
        unique=True,
        null=False,
        blank=False
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        null=False,
        blank=False
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=MUSICS,
        null=False,
        blank=False,

    )

    description = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=(validators.MinValueValidator(0.0),),
        null=False,
        blank=False
    )

    class Meta:
        ordering = ('pk',)

