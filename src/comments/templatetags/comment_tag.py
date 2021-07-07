from django import template
from django.contrib.contenttypes.models import ContentType
from .. import models

register = template.Library()


@register.inclusion_tag('comments/tags/show_comments.html', takes_context=True)
def show_comments(context):
    object = context.get('object')
    next_step = context.get('request').path
    content_type = ContentType.objects.get_for_model(object)
    content_type_id = content_type.pk
    comments = models.Comment.objects.filter(content_type=content_type, object_id=object.pk)
    return {'comments': comments, 'next_step': next_step, 'content_type_id': content_type_id, 'object_id':object.pk}