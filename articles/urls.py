from django.conf.urls import url
from .import views

# for removing headache of same domain use 'app_name'
app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name='list'),
    url(r'^create',views.create_article,name='create'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail, name='detail')
]



# [\w-]+  means it can be a-z/A-Z or 0-9