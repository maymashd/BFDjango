from django.core.management.base import BaseCommand
from datetime import datetime
import random

from main.models import Task


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of products for creation')

        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new products')

        parser.add_argument('-e', '--exp', action='store_true', help='Create Product with expensive price')


    def handle(self, *args, **kwargs):
        # Product.objects.all().delete()

        self.stdout.write(f"kwargs:{kwargs['total']} ")
        total = kwargs['total']
        prefix = kwargs.get('prefix')
        expensive = kwargs.get('exp')

        if not prefix:
            prefix = 'AA'

        for i in range(total):
                b = Task.objects.create(name=f'{prefix}_todo {i}',
                                        created_by_id=1,
                                        task_list_id=1
                                        )
                self.stdout.write(f'Todo {b.id} was created')
                #
                # objects = TaskManager()
                # name = models.CharField(max_length=200)
                # created_at = models.DateTimeField(auto_now_add=True, blank=True)
                # due_on = models.DateTimeField(default=datetime.now, blank=True)
                # status = models.CharField(max_length=50, default="in process")
                # task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name="tasks")
                # created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
                #

