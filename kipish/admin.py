from django.contrib import admin
from django.utils.safestring import mark_safe

from kipish.forms import ImagePostForm
from kipish.models import Place, ImagePost, VideoPost, ImageItem, Contact, SocialMedia


# @admin.register(ImagePost)
# class ImagePostAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#     add_form_template = 'admin/image_post_form.html'
#     change_form_template = 'admin/image_post_form.html'
#
#     def get_form(self, request, obj=None, **kwargs):
#         try:
#             instance = kwargs['instance']
#             return ImagePostForm(instance=instance)
#         except KeyError:
#             return ImagePostForm
#
#     def add_view(self, request, form_url="", extra_context=None):
#         extra_context = extra_context or {}
#         extra_context['form'] = self.get_form(request)
#         return super(ImagePostAdmin, self).add_view(request, form_url=form_url, extra_context=extra_context)
#
#     def change_view(self, request, object_id, form_url="", extra_context=None):
#         extra_context = extra_context or {}
#         post = ImagePost.objects.get(id=object_id)
#         extra_context["form"] = self.get_form(instance=post)
#         return super(ImagePostAdmin, self).change_view(request, object_id, form_url=form_url, extra_context=extra_context)
#
#     def save_model(self, request, obj, form, change):
#         obj.save()
#         pictures = request.FILES.getlist('photo')
#         for picture in pictures:
#             ImageItem.objects.create(image_posts=obj, image=picture)
#         return super().save_model(request, obj, form, change)

class ImageItemInline(admin.StackedInline):
    model = ImageItem


@admin.register(ImagePost)
class ImagePostAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title')
    inlines = [ImageItemInline]
    prepopulated_fields = {'slug': ['title']}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title')
    prepopulated_fields = {'slug': ['title']}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('get_icon', 'name')

    def get_icon(self, obj):
        return mark_safe(f'<img src={obj.icon.url} width="50" height="60"')


@admin.register(VideoPost)
class VideoPostAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Contact)
admin.site.register(ImageItem)
