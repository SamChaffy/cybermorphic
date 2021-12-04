from rest_framework.serializers import ModelSerializer
from cybermorphic.core.models import ContactMessage


class ContactSerializer(ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'subject', 'message',)
