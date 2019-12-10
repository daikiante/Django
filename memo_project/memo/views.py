from django.shortcuts import render
from .models import Memo

# Create your views here.

def index(request):
    memos = Memo.objects.order_by('-create_date')
    return render(request, 'memo/index.html', {'memos':memos})

def detail(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    return render(request, 'memo/detail.html', {'memo':memo})