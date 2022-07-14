from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f'[{self.id}] {self.firstname} {self.lastname}, {self.address}, {self.city}'


#create food model
class Food(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f'[{self.id}] {self.name}, {self.description}, {self.price}'

    def method1(self):
        return 'banana'

    def price_in_usd(self):
        return f'{self.price / 56:.2f}'


#create order model customer can only order one kind of food
class Order(models.Model):
    PAYMENT_MODE_CHOICES = [
        #tuples (an immutable list), second part is a human readable form
        ("CH", "Cash"),
        ("CD", "Card"),

    ] #common convention to uppercase variables
    orderdatetime = models.DateTimeField(auto_now_add=True) #will get current time but you can't update dates
    paymentmode = models.CharField(max_length=2, choices=PAYMENT_MODE_CHOICES) #ch for cash, cd for card and only that's accepter
    quantity = models.IntegerField()
    food = models.ForeignKey(Food, on_delete = models.CASCADE) #have to connect to food and customer, what if we delete the burger so the second part if we delete the burger record then we delete all records with burger in, you can restrict it from being delete or just set it to nulll
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.id}] {self.customer.firstname} {self.customer.lastname}, {self.food.name}, {self.quantity}, {self.paymentmode}, {self.orderdatetime}'


