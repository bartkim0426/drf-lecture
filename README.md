## Filter

**drf SearchFilter, OrderingFilter**
```python
from rest_framework.filters import SearchFilter, OrderingFilter
...
# in APIView
filter_backends = [SearchFilter, OrderingFilter]
search_fields = ['title', 'content']
```

**Q 사용하여 filter**
기존 cbv에서 사용하듯이 작성해서 사용하면 될듯
```python
    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)|
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list
```


**django-filter(3rd party library)**    

1. Install django-filter
```bash
pip install django-filter
```
2. Add django_filters in INSTALLED_APPS

3. Add DjangoFilterBackend settings in `settings.py`
```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
```

4. Use in View or ViewSet
```python
from django_filters.rest_framework import DjangoFilterBackend

class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer

	# use filter, Search, Ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'user__first_name']
    filter_fields = ['title', 'user', 'id']
	ordering_fields = ['id']
	# default ordering by
	ordering = ('publilsh',)
```
> 자동으로 FilterSet을 만들어준다. FilterSet에 대한 자세한 설명은 [Django filter documention](https://django-filter.readthedocs.io/en/latest/index.html) 참고, [drf integration](https://django-filter.readthedocs.io/en/develop/guide/rest_framework.html) 읽어보기

이런식으로 Regex 이용이 가능하다.
- '^' Starts-with search.
- '=' Exact matches.
- '@' Full-text search. (Currently only supported Django's MySQL backend.)
- '$' Regex search.

5. DjangoObjectPermissionFilter
[django-guardian](https://django-guardian.readthedocs.io/en/stable/)과 함께 쓰임. 특정 권한을 가진 사람에게 특정 object만 제공할 수 있는 기능 제공. 자세한 내용은 사용 시 drf 문서 참고해서 사용

6. 3rd party apps
relations을 따라 탐색할 수 있는 [django-rest-framework-filters](https://github.com/philipn/django-rest-framework-filters), 사용자 친화적인 url을 제공하는 [django-url-filter](https://github.com/miki725/django-url-filter) 등을 확인해보면 좋을듯
