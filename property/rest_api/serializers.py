from rest_framework import serializers

# Import the models
from .models import AccountManager, RealEstateAgency, Agent, User, Property, Station, School, City, Area, PropertyType

# The Serializer will turn our database models into JSON data


class AccountManagerSerializer(serializers.ModelSerializer):
    clients = serializers.StringRelatedField(many=True)

    class Meta:
        model = AccountManager
        fields = '__all__'


class RealEstateAgencySerializer(serializers.ModelSerializer):
    employees = serializers.StringRelatedField(many=True)

    class Meta:
        model = RealEstateAgency
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    property_portfolio = serializers.StringRelatedField(many=True)

    class Meta:
        model = Agent
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    agent = AgentSerializer(many=False, read_only=True)

    class Meta:
        model = Property
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):
    nearby_properties = serializers.StringRelatedField(many=True)

    class Meta:
        model = Station
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    city_properties = serializers.StringRelatedField(many=True)

    class Meta:
        model = City
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    in_city = serializers.StringRelatedField(many=True)

    class Meta:
        model = Area
        fields = '__all__'


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = '__all__'
