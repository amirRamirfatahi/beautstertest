from rest_framework.generics import GenericAPIView, get_object_or_404


class BaseAPIView(GenericAPIView):
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {
            self.lookup_field: self.request.data.get(self.lookup_field)
        }

        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)

        return obj


