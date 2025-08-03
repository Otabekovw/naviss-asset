from rest_framework import serializers
from . import models

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partner
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = '__all__'
