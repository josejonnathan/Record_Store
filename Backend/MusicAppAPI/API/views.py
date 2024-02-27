from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .serializers import RecordSerializer, SimpleRecordSerializer
from .models import Record


class AllRecordsView(generics.ListAPIView):
    """
    A view to retrieve a list of all records.

    Attributes:
        permission_classes (list): The list of permission classes applied to the view.
        queryset (queryset): The queryset used to retrieve records.
        serializer_class (serializer): The serializer class used to serialize records.
    """

    permission_classes = [IsAuthenticated]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordDetailView(generics.RetrieveAPIView):
    """
    A view to retrieve details of a single record.

    Attributes:
        permission_classes (list): The list of permission classes applied to the view.
        queryset (queryset): The queryset used to retrieve records.
        serializer_class (serializer): The serializer class used to serialize records.
        lookup_field (str): The field used to retrieve a record.
    """

    permission_classes = [IsAuthenticated]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    lookup_field = 'pk'


class CreateRecordsView(generics.CreateAPIView):
    """
    A view to create new records.

    Attributes:
        authentication_classes (list): The list of authentication classes applied to the view.
        permission_classes (list): The list of permission classes applied to the view.
        queryset (queryset): The queryset used to create records.
        serializer_class (serializer): The serializer class used to serialize records.
    """

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class UpdateDeleteRecordsView(generics.RetrieveUpdateDestroyAPIView):
    """
    A view to update or delete existing records.

    Attributes:
        authentication_classes (list): The list of authentication classes applied to the view.
        permission_classes (list): The list of permission classes applied to the view.
        queryset (queryset): The queryset used to update or delete records.
        serializer_class (serializer): The serializer class used to serialize records.
    """

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class SimpleRecordsView(generics.ListAPIView):
    """
    A view to retrieve a list of simple records.

    Attributes:
        authentication_classes (list): The list of authentication classes applied to the view.
        permission_classes (list): The list of permission classes applied to the view.
        queryset (queryset): The queryset used to retrieve simple records.
        serializer_class (serializer): The serializer class used to serialize simple records.
    """

    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Record.objects.all()
    serializer_class = SimpleRecordSerializer
