from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


# First model definition
class Task(models.Model):
    # Mandatory title field
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    # Mandatory desc field
    description = models.TextField()
    # Mandatory owner field
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # optional story point field
    story_point = models.PositiveSmallIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return '%s : %s' % (self.title, self.description)


# Second model definition with predefined choices.
class Status(models.Model):
    # The status parameters are predefined and had been implemented in  server-side.
    # In order to view meaningful status to user in detail page, I haven't used integers/abbreviation.
    status_list = (
        ('Open', 'Open'),
        ('InProgress', 'In progress'),
        ('Review', 'Review'),
        ('Test', 'Test'),
        ('Done', 'Done'),
    )
    # with defining choices, we can have a dropdown menu in ui page with predefined status options.
    status = models.CharField(max_length=20, choices=status_list, default=0)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.status
