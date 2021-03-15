from rest_framework import routers
from .api import AccountManagerViewSet, RealEstateAgencyViewSet, AgentViewSet, UserViewSet, PropertyViewSet, StationViewSet, SchoolViewSet, CityViewSet, AreaViewSet, PropertyTypeViewSet

router = routers.DefaultRouter()
router.register('api/account-managers',
                AccountManagerViewSet, 'account manager')
router.register('api/real-estate-agencies',
                RealEstateAgencyViewSet, 'real estate agencies')
router.register('api/agents', AgentViewSet, 'agents')
router.register('api/users', UserViewSet, 'users')
router.register('api/properties', PropertyViewSet, 'properties')
router.register('api/stations', StationViewSet, 'stations')
router.register('api/schools', SchoolViewSet, 'schools')
router.register('api/cities', CityViewSet, 'cities')
router.register('api/areas', AreaViewSet, 'areas')
router.register('api/property-types', PropertyTypeViewSet, 'property types')


urlpatterns = router.urls
