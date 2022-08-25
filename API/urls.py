from django.urls import path, include
from API.views import ParserView, PostApiView, TagApiView
from rest_framework.routers import DefaultRouter
from .yasg import urlpatterns as doc_urls

router = DefaultRouter()
router.register(r'news', PostApiView)
router.register(r'tags', TagApiView)

urlpatterns = [
    path('parse/', ParserView.as_view()),
    path('', include(router.urls))
]

urlpatterns += doc_urls