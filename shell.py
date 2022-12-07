from daamduu.models import *

client1 = Client.objects.create(user=User.objects.create(email='nikname21@gmail.com', password='defender42'), name='Азат Соколов', card_number='4147565798789009')
worker1 = Worker.objects.create(user=User.objects.create(email='altywa1998@gmail.com', password='nono34'), name='Алтынай Алиева', position='Оператор кассы')

food1 = Food.objects.create(name='Shaurma', start_price=50)
food2 = Food.objects.create(name='Humburger', start_price=25)

ingredient1 = Ingredient.objects.create(name='Сыр', extra_price=10)
ingredient2 = Ingredient.objects.create(name='курица', extra_price=70)
ingredient3 = Ingredient.objects.create(name='говядина', extra_price=80)
ingredient4 = Ingredient.objects.create(name='салат', extra_price=15)
ingredient5 = Ingredient.objects.create(name='фри', extra_price=15)

food1.ingredients.set([ingredient1, ingredient3, ingredient4, ingredient5],
                      through_defaults={'client':client1, 'worker':worker1}
                      )



order1_bill = food1.start_price + ingredient1.extra_price + ingredient3.extra_price + ingredient4.extra_price + ingredient5.extra_price
print(order1_bill)

food2.ingredients.set([ingredient2, ingredient4],
                      through_defaults={'client': client1, 'worker': worker1})

order2_bill = food2.start_price + ingredient2.extra_price + ingredient4.extra_price
print(order2_bill)


