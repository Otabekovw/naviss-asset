from rest_framework import generics, viewsets
from . import models
from . import Serializers

class PartnersAPIView(generics.ListAPIView):
    queryset = models.Partners.objects.all()
    serializer_class = Serializers.UserProfileSerializers

class PartnersCreateAPIView(generics.CreateAPIView):
    queryset = models.Partners.objects.all()
    serializer_class = Serializers.UserProfileSerializers

class PartnersUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Partners.objects.all()
    serializer_class = Serializers.UserProfileSerializers

class PartnersDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Partners.objects.all()
    serializer_class = Serializers.UserProfileSerializers

class NewsAPIView(generics.ListAPIView):
    queryset = models.News.objects.all()
    serializer_class = Serializers.NewsSerializers

class ContactAPIView(generics.ListAPIView):
    queryset = models.Contacts.objects.all()
    serializer_class = Serializers.ContactsSerializers

class ApplicationsAPIView(generics.ListAPIView):
    queryset = models.Applications.objects.all()
    serializer_class = Serializers.ApplicationsSerializers

class ReviewAPIView(generics.ListAPIView):
    queryset = models.Review.objects.all()
    serializer_class = Serializers.ReviewSerializers

class DetailednewsAPIView(generics.ListAPIView):
    queryset = models.Detailednews.objects.all()
    serializer_class = Serializers.DetailednewsSerializers

class DetailednewsDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Detailednews.objects.all()
    serializer_class = Serializers.DetailednewsSerializers





