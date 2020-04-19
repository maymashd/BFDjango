from django.core.management.base import BaseCommand

from main.models import Category, Product


def create_authors(num):
    categories = [Category(name=f'my_category {i}')
                  for i in range(num)]

    Category.objects.bulk_create(categories)


class Command(BaseCommand):
    help = 'Delete Products from table'

    def add_arguments(self, parser):
        parser.add_argument('product_id', nargs='+', type=int, help='Product ids for delete')

    def handle(self, *args, **kwargs):
        product_ids = kwargs['product_id']

        for product_id in product_ids:
            try:
                p = Product.objects.get(id=product_id)
                p.delete()
                self.stdout.write(self.style.SUCCESS(f'Product id: {product_id} was deleted'))
            except Product.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Product id: {product_id} does not exit'))