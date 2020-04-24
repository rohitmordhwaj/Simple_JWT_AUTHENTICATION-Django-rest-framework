from django.conf.urls import url
from .views import StudentAPIView,StudentCreateAPIView  #,StudentDetailAPIView,StudentUpdateAPIView,StudentDeleteAPIView

urlpatterns = [
	url(r'^$', StudentAPIView.as_view()),
	url(r'^create/$', StudentCreateAPIView.as_view()),
	#url(r'^(?P<pk>\d+)/$', StudentDetailAPIView.as_view()),
	#url(r'^(?P<pk>\d+)/update/$', StudentUpdateAPIView.as_view()),
	#url(r'^(?P<pk>\d+)/delete/$', StudentDeleteAPIView.as_view()),
]
