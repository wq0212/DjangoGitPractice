from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    # Ex /blog/
    path('',views.PostLV.as_view(),name='index'),

    # Ex /blog/post/
    path('post/',views.PostLV.as_view(),name='post_list'),

    # Ex /blog/post/django-example/
    re_path(r'^post/(?P<slug>[-\w]+)/$',views.PostDV.as_view(),name='post_detail'),

    # Ex /blog/archive/
    path('archive/',views.PostAV.as_view(),name='post_archive'),

    # Ex /blog/archive/2021/
    path('archive/<int:year>/',views.PostYAV.as_view(),name='post_year_archive'),

    # Ex /blog/archive/2021/jan/
    path('archive/<int:year>/<str:month>/',views.PostMAV.as_view(),name='post_month_archive'),

    # Ex /blog/archive/2021/jan/10/
    path('archive/<int:year>/<str:month>/<int:day>/',views.PostDAV.as_view(),name='post_day_archive'),

    # Ex /blog/archive/today/
    path('archive/today/',views.PostTAV.as_view(),name='post_today_archive'),

    # Ex /blog/tag/
    path('tag/',views.TagCloudTV.as_view(),name='tag_cloud'),

    # Ex /blog/tag/tagname/
    path('tag/<str:tag>/',views.TaggedObjectLV.as_view(),name='tagged_object_list'),

]
