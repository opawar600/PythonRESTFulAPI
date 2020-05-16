from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Todo(models.Model):
    # Create a task
    todo = models.CharField(max_length=100, null=False,
                            help_text="This field is required")
    # Mark the action as complete or not complete
    action = models.PositiveSmallIntegerField(choices=((1, "Incomplete"),(2, "Complete")),default = 1)

    def __str__(self):
        return self.todo
