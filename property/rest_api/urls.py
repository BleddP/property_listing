from rest_framework import routers
from .api import AccountManagerViewSet, RealEstateAgencyViewSet, AgentViewSet, UserViewSet, PropertyViewSet, StationViewSet, SchoolViewSet, CityViewSet, AreaViewSet, PropertyTypeViewSet

router = routers.DefaultRouter()
router.register('api/account-managers',
                AccountManagerViewSet, 'account manager')
router.register('api/real-estate-agencies',
                RealEstateAgencyViewSet, 'account manager')
router.register('api/agents', AgentViewSet, 'account manager')
router.register('api/users', UserViewSet, 'account manager')
router.register('api/properties', PropertyTypeViewSet, 'account manager')
router.register('api/stations', StationViewSet, 'account manager')
router.register('api/schools', SchoolViewSet, 'account manager')
router.register('api/cities', CityViewSet, 'account manager')
router.register('api/areas', AreaViewSet, 'account manager')
router.register('api/property-types', PropertyTypeViewSet, 'account manager')


urlpatterns = router.urls
