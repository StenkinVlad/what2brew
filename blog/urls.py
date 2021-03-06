from . import views
from django.urls import path

# from django.contrib.sitemaps.views import sitemap
# from what2brew.sitemaps import PostSitemap
#
# sitemaps = {
#     "posts": PostSitemap,
# }

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('13', views.page13),
    path('about', views.about_me, name='about'),
    path('terms', views.terms, name='terms'),
    # path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    # path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
]


# urlpatterns = [
#     url(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blog/
#                                                # будет выводиться список постов
#     url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # а по URL http://имя_сайта/blog/число/
#                                               # будет выводиться пост с определенным номером
# ]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)