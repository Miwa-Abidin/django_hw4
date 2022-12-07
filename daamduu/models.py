from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='Имя')
    card_number = models.CharField(max_length=20, unique=True, verbose_name='Номер карты')

    def __str__(self):
        return self.name

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='Имя')
    position = models.CharField(max_length=20, verbose_name='Должность')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование ингредиента')
    extra_price = models.IntegerField(verbose_name='Стоимость надбавки')

    def __str__(self):
        return self.name

class Food(models.Model):
    ingredients = models.ManyToManyField(Ingredient, related_name='food', through='Order')
    name = models.CharField(max_length=25, verbose_name='Блюдо')
    start_price = models.IntegerField(verbose_name='Начальная стоимость')

    def __str__(self):
        return self.name

class Order(models.Model):
    food = models.ForeignKey(Food, related_name='food', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, related_name='orders', on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(auto_now_add=True, verbose_name='Время заказа')

    def __str__(self):
        return f'{self.food.name} - {self.ingredient.name} - {self.client.name} - {self.worker.name}'



