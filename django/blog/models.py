from django.db import models
from django.utils import timezone


class Post(models.Model):
    # 클래스 속성
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        # on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateField(
        blank=True, null=True
    )

    class Meta:
        verbose_name = '글'
        verbose_name_plural = f'{verbose_name}들'
        ordering = ['-created_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title