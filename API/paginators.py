from rest_framework.pagination import PageNumberPagination


class PostPaginator(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 1000



class TagPaginator(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000
