from django.core.management.base import BaseCommand
from datetime import datetime
import random

from main.models import Category, Product


def create_categories(num):
    categories = [Category(name=f'my_category {i}')
                  for i in range(num)]

    Category.objects.bulk_create(categories)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of products for creation')

        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new products')

        parser.add_argument('-e', '--exp', action='store_true', help='Create Product with expensive price')

    def handle(self, *args, **kwargs):
        # Product.objects.all().delete()

        total = kwargs['total']
        prefix = kwargs.get('prefix')
        expensive = kwargs.get('exp')

        if not prefix:
            prefix = 'AA'

        for i in range(total):
            if not expensive:
                b = Product.objects.create(name=f'{prefix}_product {i}',
                                           price=random.randint(500, 2000),
                                           created_at=datetime.now(),
                                           category_id=2
                                           )
            else:
                b = Product.objects.create(name=f'{prefix}_product {i}',
                                           price=10000,
                                           created_at=datetime.now(),
                                           category_id=2
                                           )
            self.stdout.write(f'Product {b.id} was created')