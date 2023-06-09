from django.db import models
from django.contrib.auth.models import User

# Represents a product in the application
# Fields: title, description, price, category, image
# Uses the CAT_CHOICES tuple to provide choices for the category field
# Contains a __str__ method that returns the title of the product
CAT_CHOICES = (
    ('AR','Art'),
    ('RP','Realistic Picture'),
    ('O','Other')
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.TextField(choices=CAT_CHOICES, max_length=2) 
    image = models.ImageField(upload_to='Product')
    def __str__(self):
        return self.title

# Represents a customer in the application
# Fields: user (foreign key to User model), firstname, lastname, email, phonenumber
# Contains a __str__ method that returns the first name of the customer
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.CharField(max_length=100, default='')
    phonenumber = models.CharField(max_length=15, default='')
    def __str__(self):
        return self.firstname

# Represents a cart item in the application
# Fields: user (foreign key to User model), product (foreign key to Product model), quantity
# Contains a totalcost property that calculates the total cost of the cart item
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def totalcost(self):
        return self.quantity * self.product.price

# Represents an order in the application
# Fields: user (foreign key to User model), first_name, last_name, email, product_names, status, created_at
# Uses the STATUS_CHOICES tuple to provide choices for the status field
# Contains a __str__ method that returns the order number
class Order(models.Model):
    STATUS_CHOICES = (
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    product_names = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='In Progress')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk}"