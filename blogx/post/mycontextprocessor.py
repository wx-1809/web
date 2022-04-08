#coding=utf-8

from django.db.models import Count

from post.models import Post


def getRightInfo(request):


    #1.获得分类信息
    r_catepost = Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by('-c')

    #2.近期文章
    r_recpost = Post.objects.all().order_by('-created')[:3]

    #3.获取日期归档日期
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SET sql_mode=(SELECT REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY', ''));") #解决mysql 8 ERROR 1055 (42000) error
    cursor.execute("select created,count('*') c from t_post GROUP BY DATE_FORMAT(created,'%Y-%m') ORDER BY c desc,created desc")
    r_filepost = cursor.fetchall() #

    return {'r_catepost': r_catepost,'r_recpost': r_recpost, 'r_filepost': r_filepost}