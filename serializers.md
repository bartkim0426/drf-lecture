The [django-rest-marshmallow](http://tomchristie.github.io/django-rest-marshmallow/) package provides an alternative implementation for serializers, using the python [marshmallow](https://marshmallow.readthedocs.io/en/latest/) library. It exposes the same API as the REST framework serializers, and can be used as a drop-in replacement in some use-cases.

## [Serpy](http://www.django-rest-framework.org/api-guide/serializers/#serpy)

The [serpy](https://github.com/clarkduvall/serpy) package is an alternative implementation for serializers that is built for speed. [Serpy](https://github.com/clarkduvall/serpy) serializes complex datatypes to simple native types. The native types can be easily converted to JSON or any other format needed.

## [MongoengineModelSerializer](http://www.django-rest-framework.org/api-guide/serializers/#mongoenginemodelserializer)

The [django-rest-framework-mongoengine](https://github.com/umutbozkurt/django-rest-framework-mongoengine) package provides a `MongoEngineModelSerializer` serializer class that supports using MongoDB as the storage layer for Django REST framework.

## [GeoFeatureModelSerializer](http://www.django-rest-framework.org/api-guide/serializers/#geofeaturemodelserializer)

The [django-rest-framework-gis](https://github.com/djangonauts/django-rest-framework-gis) package provides a `GeoFeatureModelSerializer` serializer class that supports GeoJSON both for read and write operations.

## [HStoreSerializer](http://www.django-rest-framework.org/api-guide/serializers/#hstoreserializer)

The [django-rest-framework-hstore](https://github.com/djangonauts/django-rest-framework-hstore) package provides an `HStoreSerializer` to support [django-hstore](https://github.com/djangonauts/django-hstore) `DictionaryField` model field and its `schema-mode` feature.

## [Dynamic REST](http://www.django-rest-framework.org/api-guide/serializers/#dynamic-rest)

The [dynamic-rest](https://github.com/AltSchool/dynamic-rest) package extends the ModelSerializer and ModelViewSet interfaces, adding API query parameters for filtering, sorting, and including / excluding all fields and relationships defined by your serializers.

## [Dynamic Fields Mixin](http://www.django-rest-framework.org/api-guide/serializers/#dynamic-fields-mixin)

The [drf-dynamic-fields](https://github.com/dbrgn/drf-dynamic-fields) package provides a mixin to dynamically limit the fields per serializer to a subset specified by an URL parameter.

## [DRF FlexFields](http://www.django-rest-framework.org/api-guide/serializers/#drf-flexfields)

The [drf-flex-fields](https://github.com/rsinger86/drf-flex-fields) package extends the ModelSerializer and ModelViewSet to provide commonly used functionality for dynamically setting fields and expanding primitive fields to nested models, both from URL parameters and your serializer class definitions.

## [Serializer Extensions](http://www.django-rest-framework.org/api-guide/serializers/#serializer-extensions)

The [django-rest-framework-serializer-extensions](https://github.com/evenicoulddoit/django-rest-framework-serializer-extensions) package provides a collection of tools to DRY up your serializers, by allowing fields to be defined on a per-view/request basis. Fields can be whitelisted, blacklisted and child serializers can be optionally expanded.

## [HTML JSON Forms](http://www.django-rest-framework.org/api-guide/serializers/#html-json-forms)

The [html-json-forms](https://github.com/wq/html-json-forms) package provides an algorithm and serializer for processing `<form>`submissions per the (inactive) [HTML JSON Form specification](https://www.w3.org/TR/html-json-forms/). The serializer facilitates processing of arbitrarily nested JSON structures within HTML. For example, `<input name="items[0][id]" value="5">` will be interpreted as `{"items": [{"id": "5"}]}`.

## [DRF-Base64](http://www.django-rest-framework.org/api-guide/serializers/#drf-base64)

[DRF-Base64](https://bitbucket.org/levit_scs/drf_base64) provides a set of field and model serializers that handles the upload of base64-encoded files.

## [QueryFields](http://www.django-rest-framework.org/api-guide/serializers/#queryfields)

[djangorestframework-queryfields](http://djangorestframework-queryfields.readthedocs.io/) allows API clients to specify which fields will be sent in the response via inclusion/exclusion query parameters.

## [DRF Writable Nested](http://www.django-rest-framework.org/api-guide/serializers/#drf-writable-nested)

The [drf-writable-nested](http://github.com/beda-software/drf-writable-nested) package provides writable nested model serializer which allows to create/update models with nested related data.
