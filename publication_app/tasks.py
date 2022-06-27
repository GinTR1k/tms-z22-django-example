from django.core.cache import cache
from celery import shared_task


@shared_task
def very_long_task():
    result = cache.get('very_long_task300000')
    if result:
        return str(result) + ' (cached)'

    fact = 1

    for i in range(1, 300000):
        fact = fact * i

    cache.set("very_long_task300000", fact, 60*5)
    return fact
