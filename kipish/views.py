from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from kipish.models import Place, ImagePost, Contact, VideoPost, SaveIp

class HomePage(View):
    def get(self, request):
        photo = ImagePost.objects.filter(top=True)[:12]
        video = VideoPost.objects.filter(top=True)[:4]
        context = {'photo': photo, 'video': video}
        return render(request, 'index.html', context)


class PlaceListView(View):
    def get(self, request):
        place_list = Place.objects.all()
        top_place = Place.objects.filter(top=True)
        context = {'place_list': place_list, 'top_place': top_place}
        return render(request, 'place_list.html', context)


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'place_detail.html'
    context_object_name = 'place'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_post_list'] = ImagePost.objects.filter()
        return context


class ImagePostListView(ListView):
    model = ImagePost
    template_name = 'photo_list.html'
    context_object_name = 'image_posts'


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def image_detail_view(request, slug):
    image_post = ImagePost.objects.get(slug=slug)
    ip = get_client_ip(request)

    if SaveIp.objects.filter(ip=ip).exists():
        image_post.views.add(SaveIp.objects.get_or_create(ip=ip))

    context = {'image_post': image_post}
    return render(request, 'photo_detail.html', context)


def video_detail_view(request, slug):
    video_post = VideoPost.objects.get(slug=slug)

    ip = get_client_ip(request)

    if SaveIp.objects.filter(ip=ip).exists():
        video_post.views.add(SaveIp.objects.get_or_create(ip=ip))

    context = {'video': video_post}
    return render(request, 'video_detail.html', context)


class VideoPostListView(ListView):
    model = VideoPost
    template_name = 'video_list.html'
    context_object_name = 'video_posts'


class VideoPostDetailView(DetailView):
    model = VideoPost
    template_name = 'video_detail.html'
    context_object_name = 'video'


class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contact_list'


class SearchResultsView(ListView):
    model = ImagePost
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = ImagePost.objects.filter(title__icontains=query)
        return object_list
