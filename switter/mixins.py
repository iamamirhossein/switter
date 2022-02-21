from django.http import Http404


class FieldsMixin:

    def dispatch(self, request, *args, **kwargs):
        self.fields = ['body', 'draft', 're_sweet', ]

        return super().dispatch(request, *args, **kwargs)


class FormValidMixin:

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.user = self.request.user

        return super().form_valid(form)
