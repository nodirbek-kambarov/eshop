from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='authors')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class PostTagModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post tag'
        verbose_name_plural = 'post tags'


class PostModel(models.Model):
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to='posts')
    banner = models.ImageField(upload_to='post banners')
    author = models.ForeignKey(AuthorModel,
                               on_delete=models.PROTECT,
                               related_name='posts'
                               )
    content = RichTextUploadingField()
    tags = models.ManyToManyField(PostTagModel,
                                  related_name='posts'
                                  )
    created_at = models.DateTimeField(auto_now_add=True)

    def get_comments(self):
        return self.comments.order_by('-created_at')

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class CommentModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    comment = models.TextField()
    post = models.ForeignKey(PostModel,
                             on_delete=models.CASCADE,
                             related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} | {self.post.title}'

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
