import math
from django.shortcuts import render

# Create your views here.
from post import models
from django.core.paginator import Paginator

def queryAll(request,num=1):
    num = int(num)
    #获取所有帖子信息
    postlist = models.Post.objects.all().order_by('-create')

    #创建分页器对象
    pageObj = Paginator(postlist, per_page = 1)

    #获取当前页数据
    perPageList = pageObj.page(num)

    #生成页码数列表
    #每页开始页码
    begin = (num-int(math.ceil(10.0 / 2)))

    if begin < 1:
        begin = 1

    #每页结束页码
    end = begin + 9
    if end > pageObj.num_pages:
        end = pageObj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pagelist = range(begin, end + 1)

    return render(request, 'index.html', {'postlist':perPageList, 'pagelist': pagelist, 'currentNum':num})

#阅读全文gongn
def detail(request,postid):
    postid = int(postid)
    #根据postid查询帖子详情
    post = models.Post.objects.get(id=postid)
    return render(request, 'detail.html', {'post':post})