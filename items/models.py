from django.db import models


currencies = (('rub', 'RUB'), ('usd', 'USD'))


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(max_length=3, choices=currencies, default='usd')

    def __str__(self):
        return self.name

    def get_price(self):
        return self.price / 100

    def get_pair_item_id(self):
        if self.currency == 'usd':
            return Item.objects.get(name=self.name, currency='rub').id
        if self.currency == 'rub':
            return Item.objects.get(name=self.name, currency='usd').id

    class Meta:
        unique_together = ('name', 'currency')
