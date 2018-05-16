from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/vote/end_form/', views.EndFormView.as_view(), name='end_form'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('finalresults', views.get_finalacc, name='fresults'),
] 
