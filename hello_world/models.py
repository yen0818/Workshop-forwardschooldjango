from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    # A one-to-one relationship. Conceptually, this is similar to a ForeignKey with unique=True, 
    # but the "reverse" side of the relation will directly return a single object.

    # ON DELETE CASCADE constraint is used in MySQL to delete the rows from the child table automatically, 
    # when the rows from the parent table are deleted.

    occupation = models.TextField(blank=True)
    company = models.TextField(blank=True)
    hobby = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
