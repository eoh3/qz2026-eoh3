from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Article, Attachment, AuditLog

@receiver(post_save, sender=Article)
def log_article_save(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(action=f"创建文章：{instance.title}")
    else:
        AuditLog.objects.create(action=f"更新文章：{instance.title}")

@receiver(pre_delete, sender=Article)
def log_article_delete(sender, instance, **kwargs):
    if not instance.is_deleted:
        AuditLog.objects.create(action=f"删除文章：{instance.title}")