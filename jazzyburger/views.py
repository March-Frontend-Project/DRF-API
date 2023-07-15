from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer, UserSerializer
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth import authenticate, login, logout
# from django.http import JsonResponse





class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(image=self.request.data.get('image'))  # Save the uploaded image

    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return self.serializer_class
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        return Response({'data': data})


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    
    

# class CustomLoginView(LoginView):
#     def form_valid(self, form):
#         remember_me = form.cleaned_data.get('remember_me', False)
#         if not remember_me:
#             self.request.session.set_expiry(0)
#         return super().form_valid(form)

# class CustomLogoutView(LogoutView):
#     def dispatch(self, request, *args, **kwargs):
#         logout(request)
#         return JsonResponse({'message': 'Logged out successfully.'})

