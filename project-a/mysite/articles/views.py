from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, Http404
from .models import Article, Attachment, AuditLog

def article_list(request):
    """文章列表页，过滤掉已删除的文章"""
    articles = Article.objects.filter(is_deleted=False)
    logs = AuditLog.objects.order_by('-timestamp')[:10]
    return render(request, 'articles/article_list.html', {
        'articles': articles,
        'logs': logs
    })

def article_soft_delete(request, pk):
    """软删除文章"""
    article = get_object_or_404(Article, pk=pk)
    article.is_deleted = True
    article.save()
    return redirect('article_list')

def attachment_download(request, pk):
    """附件下载"""
    attachment = get_object_or_404(Attachment, pk=pk)
    try:
        response = FileResponse(open(attachment.file.path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{attachment.file.name}"'
        return response
    except FileNotFoundError:
        raise Http404("文件不存在")