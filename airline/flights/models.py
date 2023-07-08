from django.db import models

''' A model is a class that represents a table in our database. Each attribute of the class represents a field in the table.'''

''' migration is the process of propogating changes you make to your models 
(adding a field, deleting a model, etc.) into your database schema. It is also creating the database schema for the first time.
so it's  2 steps creating and upadating the database schema.'''   

# Creating flight model that has three fields: origin, destination, and duration
# we will migrate this model to the database.

#  lets do airport model
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    #  any function can use the __str__ method to get a string representation of any object.
    def __str__(self):
        return f"{self.city} ({self.code})"
    
 # lets  do flight model using a foreign key
class Flight(models.Model):
    # models.CASCADE means that if an airport is deleted, all of its flights will be deleted as well.
    # We provide a related name, which gives us a way to search for all flights with a given airport as their origin or destination.

    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    #  any function can use the __str__ method to get a string representation of any object.
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"


    ''' inital implementation Flight model

    class Flight(models.Model):
        origin = models.CharField(max_length=64)
        destination = models.CharField(max_length=64)
        duration = models.IntegerField()  
    '''

   