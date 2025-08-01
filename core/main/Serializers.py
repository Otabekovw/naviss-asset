from rest_framework import serializers
from .models import Partners, Applications, Review, Detailednews, Contacts, News

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class ContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

class ApplicationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Applications
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class DetailednewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Detailednews
        fields = '__all__'
