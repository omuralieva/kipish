from django.urls import path


from kipish.views import PlaceListView, ImagePostListView, PlaceDetailView, ContactListView, VideoPostListView, \
     HomePage, image_detail_view, video_detail_view

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('places/', PlaceListView.as_view(), name='places'),
    path('places/<slug:slug>/', PlaceDetailView.as_view(), name='place-detail'),
    path('photo/<slug:slug>/', image_detail_view, name='photo-detail'),
    path('video/<slug:slug>/', video_detail_view, name='video-detail'),
    path('photo/', ImagePostListView.as_view(), name='photo'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('video/', VideoPostListView.as_view(), name='video'),
]

