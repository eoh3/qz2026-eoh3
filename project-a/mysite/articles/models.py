from django.db import models
import os


# 2. 文章模型
class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', '草稿 (Draft)'),
        ('in_review', '审核中 (In Review)'),
        ('published', '已发布 (Published)'),
        ('archived', '已归档 (Archived)'),
    ]

    title = models.CharField('标题', max_length=200)
    content = models.TextField('正文')
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='articles', verbose_name='作者')
    status = models.CharField('状态', max_length=20, choices=STATUS_CHOICES, default='draft')
    views = models.PositiveIntegerField('浏览量', default=0)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# 3. 附件模型（加回来了）
class Attachment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='attachments', verbose_name='关联文章')
    file = models.FileField('文件', upload_to='attachments/%Y/%m/')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '附件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return os.path.basename(self.file.name)

# 4. 审计日志模型
class AuditLog(models.Model):
    action = models.CharField('操作动作', max_length=255)
    timestamp = models.DateTimeField('时间', auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = '审计日志'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.action