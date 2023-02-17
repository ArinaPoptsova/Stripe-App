from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item


@receiver(post_save, sender=Item)
def create_pair_for_item(sender, instance, created, **kwargs):
    pairs = Item.objects.filter(name=instance.name)
    if len(pairs) < 2:
        if created:
            if instance.currency == 'usd':
                Item.objects.create(name=instance.name,
                                    description=instance.description,
                                    price=instance.price*75,
                                    currency='rub')
            elif instance.currency == 'rub':
                Item.objects.create(name=instance.name,
                                    description=instance.description,
                                    price=round(instance.price*0.013, 2),
                                    currency='usd')
