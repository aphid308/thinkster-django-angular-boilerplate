from django.conf.urls import patterns, url
from rest_framework_nested import routers
from authentication.views import AccountViewSet
from thinkster_django_angular_boilerplate.views import IndexView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',

    url('^.*$', IndexView.as_view(), name='index'),
    url(r'^api/v1/', include(router.urls)),
    url('^,*$', IndexView.as_view(), name='index'),
)
