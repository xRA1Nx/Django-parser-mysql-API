from django.db.models import Q
from rest_framework.response import Response
from data_parser.yandex import get_yandex_data
from data_parser.ozon import get_ozon_data
from rest_framework.views import APIView
from rest_framework import viewsets
from APP.models import Post, Tag
from .serializers import PostSerializer, PostListSerializer, PostAddSerializer, TagSerializer
from .paginators import PostPaginator, TagPaginator
from .filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend
import locale


# Create your views here.
class ParserView(APIView):

    def get(self, request):
        print(locale.getlocale())
        query_tags = Tag.objects.all()
        query_posts = Post.objects.all()
        data = get_yandex_data() + get_ozon_data()
        tag_set = set()

        # формируем уникальное множество тагов
        for post_data in data:
            tags = {tag for tag in post_data['tags']}
            tag_set |= tags

        # наполняем таблицу тагами
        for tag in tag_set:
            if not query_tags.filter(name=tag).exists():  # если такого тага еще нет
                Tag.objects.create(name=tag)
                print(f'добавлен tag: {tag}')

        # наполняем таблицу post
        for post_data in data:
            title = post_data['title']
            text = post_data['text']
            description = post_data['description']
            date = post_data['date']
            source = post_data['source']
            if not query_posts.filter(Q(title=title) & Q(date=date)).exists():
                p = Post.objects.create(
                    title=title,
                    description=description,
                    text=text,
                    date=date,
                    source=source
                )
                tags = {Tag.objects.get(name=tag) for tag in post_data['tags']}
                p.tags.add(*tags)

        return Response('данные обновлены')


class PostApiView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

    # filterset_fields = ['tags', 'date']

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'retrieve':
            return PostSerializer
        else:
            return PostAddSerializer


class TagApiView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TagPaginator
