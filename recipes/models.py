from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    CATEGORY_CHOICES = [
    ('main_course', 'Main Course'),
    ('dessert', 'Dessert'),
    ('vegan', 'Vegan'),
    ('appetizer', 'Appetizer'),
    ('snack', 'Snack'),
    ('soup', 'Soup'),
    ('salad', 'Salad'),
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    ('side_dish', 'Side Dish'),
    ('beverage', 'Beverage'),
    ('gluten_free', 'Gluten Free'),
    ('low_carb', 'Low Carb'),
    ('high_protein', 'High Protein'),
    ('slow_cooker', 'Slow Cooker'),
    ('grill', 'Grill'),
    ('bake', 'Bake'),
    ('stir_fry', 'Stir Fry'),
    ('raw', 'Raw'),
    ('holiday', 'Holiday'),
    ('comfort_food', 'Comfort Food'),
    ('international', 'International'),
    ('quick_meal', 'Quick Meal'),
    ('meal_prep', 'Meal Prep'),
]


    owner = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='main_course')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'name']  

    def __str__(self):
        return f'{self.name} by {self.owner}'
