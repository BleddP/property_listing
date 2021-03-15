from rest_api.models import AccountManager, RealEstateAgency, Agent, User, Property, Station, School, City, Area, PropertyType
from rest_framework import viewsets, permissions
from .serializers import AccountManagerSerializer, RealEstateAgencySerializer, AgentSerializer, UserSerializer, PropertySerializer, StationSerializer, SchoolSerializer, CitySerializer, AreaSerializer, PropertyTypeSerializer

# Account Manager Viewset
# The Viewset builds a CRUD API without having to specify the methods


class AccountManagerViewSet(viewsets.ModelViewSet):
    queryset = AccountManager.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AccountManagerSerializer


class RealEstateAgencyViewSet(viewsets.ModelViewSet):
    queryset = RealEstateAgency.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RealEstateAgencySerializer


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AgentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PropertySerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StationSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SchoolSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CitySerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AreaSerializer


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PropertyTypeSerializer
