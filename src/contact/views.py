from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import ugettext_lazy as _
from .serializers import ContactSerializer


class ContactView(GenericAPIView):

    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        # Create a serializer with request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        # Return the success message with OK HTTP status
        return Response(
            {'detail': _('Thanks for your message!')},
            status=status.HTTP_200_OK
        )


contact_view = ContactView.as_view()
