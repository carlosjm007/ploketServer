from django.conf.urls import url, include
import django.contrib.auth.views
from rest_framework import routers
import TEST.views as TestViews

router = routers.DefaultRouter()
router.register(r'jugador', TestViews.JugadorViewSet,)

snippet_detail = TestViews.UserViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy'
})
urlpatterns = [
	url(r'^api/', include(router.urls)),
	url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
]