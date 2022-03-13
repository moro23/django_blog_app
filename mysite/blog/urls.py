from django.urls import path 
from . import function_views
from .views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    ##string pattern, view, optional name for project-wide URL 
    #path('', function_views.post_list, name='post_list'),
    path('', PostListView.as_view(), name='post_list'),
    #path('<int:year>/<int:month>/<int:day>/<slug:post>/', PostDetailView.as_view(), name='post_detail')
    #path('<int:pk>', PostDetailView.as_view(), name='post_detail')
    path('<uuid:pk>/<slug:post>', PostDetailView.as_view(), name='post_detail')
    #path('<int:year>/<int:month>/<int:day>/<slug:post>/', function_views.post_detail, name='post_detail'),
]