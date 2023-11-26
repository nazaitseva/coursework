from django.core.management.base import BaseCommand
from base.models import BlogPost, Comment 

class Command(BaseCommand):
    help = 'Вычисляет общее количество комментариев для каждого поста'

    def handle(self, *args, **options):
        post_ids = BlogPost.objects.values_list('id', flat=True)

        for post_id in post_ids:
            comment_count = Comment.objects.filter(post_id=post_id).count()
            self.stdout.write(self.style.SUCCESS(f"Общее количество комментариев для новости с ID {post_id}: {comment_count}"))