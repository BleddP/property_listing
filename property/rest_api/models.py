from django.db import models

# Create your models here.


class AccountManager(models.Model):
    account_manager_employee_id: models.CharField(max_length=10, unique=True)
    account_manager_first_name: models.CharField(max_length=15)
    account_manager_last_name: models.CharField(max_length=30)
    account_manager_email: models.CharField(max_length=30)
    account_manager_phone: models.IntegerField()
    account_manager_join_date: models.DateField()
    account_manager_total_revenue: models.IntegerField()
    account_manager_this_year_revenue: models.IntegerField()
    account_manager_last_year_revenue: models.IntegerField()
    account_manager_last_quarter_revenue: models.IntegerField()
    account_manager_last_week_revenue: models.IntegerField()

    def __str__(self):
        return f'{self.account_manager_first_name} {self.account_manager_last_name}'


class RealEstateAgency(models.Model):
    name = models.CharField(max_length=30, unique=True, null=True)
    address_line_1 = models.CharField(max_length=30)
    address_line_2 = models.CharField(max_length=30, blank=True)
    address_line_3 = models.CharField(max_length=30, blank=True)
    postcode = models.CharField(max_length=30)
    area = models.ForeignKey(
        "Area", on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(
        "City", on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.CharField(max_length=30, blank=True)
    longitude = models.CharField(max_length=30, blank=True)
    website = models.CharField(max_length=30, blank=True)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    account_manager = models.ForeignKey(
        "AccountManager", on_delete=models.CASCADE, null=True, blank=True, related_name='clients')
    MEMBERSHIP_LEVELS = (
        ('Standard', 'Standard'),
        ('Professional', 'Professional'),
        ('Expert', 'Expert'),
    )
    membership_level = models.CharField(
        max_length=30, choices=MEMBERSHIP_LEVELS, default='standard')
    joined_date = models.DateField()
    subscription_expiry = models.DateField()
    blacklisted = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    industry_affiliations = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.name}'


class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=25)
    line = models.CharField(max_length=25, blank=True)
    whatsapp = models.CharField(max_length=25, blank=True)
    wechat = models.CharField(max_length=25, blank=True)
    skype = models.CharField(max_length=25, blank=True)
    agency = models.ForeignKey(
        "RealEstateAgency", on_delete=models.CASCADE, related_name='employees')  # An agent can only have one employer
    experience = models.IntegerField()
    address_line_1 = models.CharField(max_length=30)
    address_line_2 = models.CharField(max_length=30, blank=True)
    address_line_3 = models.CharField(max_length=30, blank=True)
    postcode = models.CharField(max_length=30)
    # An agent can only have one city
    city = models.ForeignKey(
        "City", on_delete=models.CASCADE, related_name='agents')
    latitude = models.CharField(max_length=30, blank=True)
    longitude = models.CharField(max_length=30, blank=True)
    website = models.CharField(max_length=30, blank=True)
    industry_affiliations = models.CharField(max_length=30, blank=True)
    blacklisted = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.agency}'


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=25, blank=True)
    blacklisted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Property(models.Model):
    published = models.BooleanField(default=False)
    property_id = models.CharField(max_length=30, blank=True)
    property_available = models.BooleanField(default=False)
    property_sold = models.BooleanField(default=False)
    property_name = models.CharField(max_length=30, blank=True)
    building_name = models.CharField(max_length=30, blank=True)
    address_line_1 = models.CharField(max_length=30)
    address_line_2 = models.CharField(max_length=30, blank=True)
    address_line_3 = models.CharField(max_length=30, blank=True)
    postcode = models.CharField(max_length=30)
    area = models.ForeignKey(
        "Area", on_delete=models.CASCADE, blank=True, null=True, related_name='nearby_properties')  # A property can only have one Area
    city = models.ForeignKey(
        "City", on_delete=models.CASCADE, blank=True, null=True, related_name='city_properties')  # A property can only have one City
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    property_type = models.ForeignKey(
        "PropertyType", on_delete=models.CASCADE, related_name="properties", blank=True, null=True)  # A property can only have one property type
    which_floor = models.IntegerField()
    total_square_m = models.IntegerField()
    total_square_ft = models.IntegerField()
    total_square_ping = models.IntegerField()
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    images = models.CharField(max_length=50, blank=True)
    property_description_short = models.CharField(max_length=500)
    property_description_long = models.CharField(max_length=1500)
    nearby_stations = models.ForeignKey(
        "Station", on_delete=models.CASCADE, related_name="nearby_properties", blank=True, null=True)
    nearby_schools = models.ForeignKey(
        "School", on_delete=models.CASCADE, related_name="nearby_properties", blank=True, null=True)
    parking_spaces = models.IntegerField()
    parking_type = models.CharField(max_length=10, blank=True)
    property_viewed = models.IntegerField()
    year_built = models.IntegerField()
    year_last_renovated = models.IntegerField(blank=True)
    previous_owners = models.IntegerField()
    developer = models.CharField(max_length=50, blank=True)
    agent = models.ForeignKey(
        "Agent", on_delete=models.CASCADE, related_name="property_portfolio")  # A property can only have one agent
    listing_date = models.DateField()
    notes = models.CharField(max_length=500, blank=True)
    key_feature_1 = models.CharField(max_length=50, blank=True)
    key_feature_2 = models.CharField(max_length=50, blank=True)
    key_feature_3 = models.CharField(max_length=50, blank=True)
    key_feature_4 = models.CharField(max_length=50, blank=True)
    key_feature_5 = models.CharField(max_length=50, blank=True)
    pdf_brochure = models.CharField(max_length=50, blank=True)
    balcony = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    concierge = models.BooleanField(default=False)
    shared_pool = models.BooleanField(default=False)
    shared_gym = models.BooleanField(default=False)
    shared_KTV = models.BooleanField(default=False)
    shared_lounge = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    baths = models.IntegerField(default=False)
    showers = models.IntegerField(default=False)
    toilets = models.IntegerField(default=False)
    dining_rooms = models.IntegerField(default=False)
    living_room = models.IntegerField(default=False)
    bedrooms = models.IntegerField(default=False)
    kitchen = models.IntegerField(default=False)
    oven = models.BooleanField(default=False)
    fridge = models.BooleanField(default=False)
    dishwasher = models.BooleanField(default=False)
    double_lock = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    washing_machine = models.BooleanField(default=False)
    free_windows = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    floorplan = models.CharField(max_length=100, blank=True)
    avatar = models.CharField(max_length=100, blank=True)
    images = models.CharField(max_length=100, blank=True)
    video = models.CharField(max_length=100, blank=True)
    property_price = models.IntegerField()
    average_increase_last_year = models.IntegerField(blank=True, null=True)
    average_increase_last_three_years = models.IntegerField(
        blank=True, null=True)
    average_increase_last_five_years = models.IntegerField(
        blank=True, null=True)
    estimated_rent = models.IntegerField(blank=True, null=True)
    estimated_yield_pct = models.IntegerField(blank=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.address_line_1}, {self.area}'


class Station(models.Model):
    station_id = models.IntegerField()
    station_name = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30, blank=True)
    longitude = models.CharField(max_length=30, blank=True)
    train_lines = models.CharField(max_length=30)
    nearby_bus_stations = models.CharField(max_length=30)
    area = models.ForeignKey(
        "Area", on_delete=models.CASCADE, blank=True, null=True)  # A Station an only have one area
    city = models.ForeignKey(
        "City", on_delete=models.CASCADE, blank=True, null=True)  # A station can only have one city

    def __str__(self):
        return f'{self.station_name}, {self.city}'


class School(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=30)
    school_type = models.CharField(max_length=30)
    area = models.ForeignKey(
        "Area", on_delete=models.CASCADE, blank=True, null=True)  # A School can only have one area
    city = models.ForeignKey(
        "City", on_delete=models.CASCADE, blank=True, null=True)  # A School can only have one City
    latitude = models.CharField(max_length=30, blank=True)
    longitude = models.CharField(max_length=30, blank=True)
    train_lines = models.CharField(max_length=30)
    nearby_bus_stations = models.CharField(max_length=30)
    average_property_price = models.IntegerField()

    def __str__(self):
        return f'{self.school_name}, {self.school_type}'


class City(models.Model):
    city_id = models.IntegerField(unique=True)
    city_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    properties = models.ForeignKey(
        "Property", on_delete=models.CASCADE, related_name="properties", blank=True, null=True)
    average_property_price = models.IntegerField()

    def __str__(self):
        return f'{self.city_name}, {self.country}'


class Area(models.Model):
    area_id = models.IntegerField(unique=True)
    area_name = models.CharField(max_length=30)
    # An area can only have one city
    city = models.ForeignKey(
        "City", on_delete=models.CASCADE, related_name='districts')
    latitude = models.CharField(max_length=30, blank=True)
    longitude = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.area_name}, {self.city}'


class PropertyType(models.Model):
    PROPERTY_TYPES = (
        ('Flat', 'Flat'),
        ('Penthouse', 'Penthouse'),
        ('Detached House', 'Detached House'),
        ('Semi-Detached House', 'Semi-Detached House'),
        ('Terraced House', 'Terraced House'),
    )
    property_type_id: models.IntegerField()
    property_type_name = models.CharField(
        max_length=30, choices=PROPERTY_TYPES, default='Flat')
    properties: models.ForeignKey("Property", on_delete=models.CASCADE,
                                  related_name="property_type_name", blank=True, null=True)

    def __str__(self):
        return f'{self.property_type_name}'
