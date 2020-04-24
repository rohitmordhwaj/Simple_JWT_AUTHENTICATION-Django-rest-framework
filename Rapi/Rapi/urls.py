
from django.contrib import admin
from django.conf.urls import url,include
from . import views 
from rest_framework_simplejwt.views import  TokenObtainPairView , TokenRefreshView

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^api/post/',include('Post.api.urls')),
	url(r'^auth/login/', TokenObtainPairView.as_view()),
	url(r'^auth/login/refresh/', TokenRefreshView.as_view()),
	url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt'))


]
