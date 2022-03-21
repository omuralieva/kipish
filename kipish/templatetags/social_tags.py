from django import template

from kipish.models import SocialMedia

register = template.Library()


@register.simple_tag()
def get_social_links():
    return SocialMedia.objects.all()
