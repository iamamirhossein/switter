from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Sweet


class FieldsMixin:

    def dispatch(self, request, *args, **kwargs):
        self.fields = ['body', 'draft', 're_sweet', ]

        return super().dispatch(request, *args, **kwargs)


class FormValidMixin:

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.user = self.request.user

        return super().form_valid(form)


class AuthorAccessMixin:

    def dispatch(self, request, pk, *args, **kwargs):

        sweet = get_object_or_404(Sweet, pk=pk)

        if sweet.user == request.user:
            return super().dispatch(request, *args, **kwargs)

        else:
            raise Http404
