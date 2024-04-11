"""Models of tasks app."""
from django.db import models


class Task(models.Model):
    """Task Model.

    Attributes:
        id (Integer): unique identificator of object
        question (TextField): a question
        answer (textField): an answer to the question
    """

    question = models.TextField()
    answer = models.TextField(default='Нет ещё ответа!!!!', blank=True)

    def save(self, *args, **kwargs) -> None:
        """Save instance to database.

        Ovverided to add complete mark.
        """
        if self.answer != '':
            self.question = '✔ ' + self.question
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        """Return what to represent when call str() method to object.

        Ovverided to return question field.
        """
        return self.question
