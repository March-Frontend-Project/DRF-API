from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from jazzyburger.views import ProductViewSet,CreateUserView

# To add image 
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/create_user/', CreateUserView.as_view(), name='create_user'),
    path('api/auth/', include('rest_framework.urls')),  # Include REST Framework's authentication URLs
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #add this for image config
