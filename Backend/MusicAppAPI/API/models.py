from django.db import models


class Record(models.Model):
    """
    Model representing a record.

    Attributes:
        title (str): The title of the record.
        artist (str): The artist of the record.
        year (int): The year of the record.
        genre (str): The genre of the record.
        deezer_id (str): The Deezer ID of the record.
        price (Decimal): The price of the record.
        available_units (int): The number of available units of the record.
    """

    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100, default='')
    deezer_id = models.CharField(max_length=50, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    available_units = models.IntegerField(default=0)

    def __str__(self):
        """
        Return a string representation of the record.

        Returns:
            str: A string representation of the record in the format 'artist - title'.
        """
        return f'{self.artist} - {self.title}'
