from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'users_and_computers'

router = NetBoxRouter()
router.register('risks', views.RiskListViewSet)
router.register('riskrelation', views.RiskRelationListViewSet)
router.register('riskassignment', views.RiskAssignmentViewSet)

urlpatterns = router.urls
