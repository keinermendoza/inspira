from django import template
from courses.models import HeroImg

register = template.Library()

@register.simple_tag
def HeroImageSource():
    return HeroImg.objects.last().src.url