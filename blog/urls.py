from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('13', views.page13),
]


# urlpatterns = [
#     url(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blog/
#                                                # будет выводиться список постов
#     url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # а по URL http://имя_сайта/blog/число/
#                                               # будет выводиться пост с определенным номером
# ]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)