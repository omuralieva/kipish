from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from kipish.models import Place, ImagePost, Contact, VideoPost


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


class ImagePostDetailView(DetailView):
    model = ImagePost
    template_name = 'photo_detail.html'
    context_object_name = 'photo'


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
