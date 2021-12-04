from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.response import Response

from cybermorphic.core.models import ContactMessage
from cybermorphic.core.serializers import ContactSerializer


class LandingView(TemplateView):
    template_name = "core/landing.html"


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        subject = f'{serializer.validated_data["name"]}  {serializer.validated_data["subject"]}'
        send_mail(
            subject,
            serializer.validated_data["message"],
            settings.EMAIL_HOST,
            ["joezeppe.code@gmail.com"],
            fail_silently=False,
        )
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)