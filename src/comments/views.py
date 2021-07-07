from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from .forms import CommentCreateForm
from .models import Comment


class CommentCreate(FormView):
    form_class = CommentCreateForm

    def form_valid(self, form):
        next_step = form.cleaned_data.get('next_step')
        text = form.cleaned_data.get('text')
        author = self.request.user
        content_type_id = form.cleaned_data.get('content_type_id')
        object_id = form.cleaned_data.get('object_id')
        content_type = ContentType.objects.get_for_id(content_type_id)
        comment = Comment.objects.create(
            author=author,
            text=text,
            content_type=content_type,
            object_id=object_id
        )
        return HttpResponseRedirect(next_step)