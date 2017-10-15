## Filter

**drf SearchFilter, OrderingFilter**
```
from rest_framework.filters import SearchFilter, OrderingFilter
...
# in APIView
filter_backends = [SearchFilter, OrderingFilter]
search_fields = ['title', 'content']
```

**Q 사용하여 filter**


**django-filter(3rd party library)**

