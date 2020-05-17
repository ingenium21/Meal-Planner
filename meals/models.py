from django.db import models

class Meal(models.Model):
    """Meal to be eaten"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        """Return a string representation of a model"""
        return. self.text

class ingredient(models.Model):
    """The ingredients that make up the meal"""
    meal = models.ForeignKey(Meal)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Ingredients'
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.text

        