from django.db import models

# Create your models here.


class Puppy(models.Model):
    """ Puppy Model Defines the attributes of a puppy."""
     
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_breed(self):
        return self.name + ' belongs to ' + self.breed + ' breed.'  # (Casper belongs to bull dog breed.)

    def __repr__(self):
        return self.name + ' is added.'

    class Meta:
        db_table = 'puppy'