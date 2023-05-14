from django.shortcuts import render, redirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .models import Chocolate
from .serializers import ChocoSerializer
from rest_framework import mixins, permissions, status
from rest_framework import generics

# Create your views here.

# class ListChocos(generics.ListCreateAPIView):
#     serializer_class = ChocoSerializer
#     queryset = Chocolate.objects.all()
#
#     def list(self,request,**kwargs):
#         queryset= self.get_queryset()
#         serializer=ChocoSerializer(queryset,many=True)
#         return Response({'object_list':queryset})

def home(request):
    return render(request,'home.html')






class ListChocolate(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='list.html'
    queryset = Chocolate.objects.all()
    serializer_class = ChocoSerializer

    def list(self,request):
        queryset=self.get_queryset()
        return Response({'object_list':queryset})

class DetailChoco(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [permissions.IsAuthenticated]
    template_name='detail.html'
    queryset=Chocolate.objects.all()

    serializer_class = ChocoSerializer

    def get(self, request, *args, **kwargs):

        queryset=self.get_object()

        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        authenticated=request.user.is_authenticated
        print('####',authenticated)

        if not authenticated:
            return redirect('list')
        return Response({'object':queryset,'authenticated':authenticated})

        # serializer=self.get_serializer(queryset)
        # return Response({'object': queryset})

class ChocoCheckoutView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [AllowAny]
    permission_classes = [permissions.IsAuthenticated]

    renderer_classes=[TemplateHTMLRenderer]
    template_name='checkout.html'
    queryset=Chocolate.objects.all()
    serializer_class=ChocoSerializer

    def get(self,request, *args, **kwargs):
        queryset=self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        authenticated=request.user.is_authenticated
        print('####',authenticated)

        if not authenticated:
            return redirect('list')
        return Response({'object':queryset,'authenticated':authenticated})




    # queryset=Chocolate.objects.all()
    # serializer_class=ChocoSerializer
    #
    # def get(self,request,*args,**kwargs):
    #     queryset=super().get(request,*args,**kwargs)
    #     serializer = self.get_serializer(queryset)
    #     return Response(serializer.data)
        # return Response({'object':queryset})