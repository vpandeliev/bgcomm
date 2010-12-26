from django import template
from django.utils.safestring import mark_safe
from posts.models import *

register = template.Library()

class RenderNode(template.Node):

    def __init__(self, content):
        self.content = content
    
    def render(self, context):
        try:
            newcontent = template.resolve_variable(self.content, context)
            return template.Template(newcontent).render(template.Context(context, autoescape=False))
        except template.TemplateSyntaxError, e:
            return mark_safe("<strong>Template error: There is an error one of this page's template tags: <code>%s</code></small>" % e.message)


@register.tag(name='render')
def render_django(parser, token):
    " Example: {% render flatpage.content %}"
    content = token.split_contents()[-1]
    return RenderNode(content)
render_django.is_safe = True


def get_execs(orderstring):
    return Executive.objects.order_by(orderstring)

register.filter('get_execs',get_execs)
