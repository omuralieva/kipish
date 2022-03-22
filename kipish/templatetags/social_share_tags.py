from django import template

from kipish.models import SocialMediaShare

register = template.Library()


@register.simple_tag()
def get_social_links():
    return SocialMediaShare.objects.all()
