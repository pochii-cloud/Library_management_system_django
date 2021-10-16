from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.views.static import serve

from core.views import base, contact, detail, search, borrow_view, borrowpage, return_view, home2, adminview, \
    delete, addview, penalty_view, baseone
from djangoProject3 import settings

urlpatterns = [
    path('', baseone, name='baseone'),
    path('base/', base, name='base'),
    path('contact/', contact, name='contact'),
    # url(r'^dowload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('dowload/', serve, {'document_root': settings.MEDIA_ROOT}),
    path('detail/<int:book_id>/', detail, name='detail'),
    path('search/', search, name='search'),
    path('borrow_view/<int:book_id>/', borrow_view, name='borrow_view'),
    path('borrowpage/', borrowpage, name='borrowpage'),
    path('return_view/<int:book_id>/', return_view, name='return_view'),
    path('home2/', home2, name='home2'),
    path('delete/<int:book_id>/', delete, name='delete'),
    path('penalty_view/<int:book_id>/', penalty_view, name='penalty_view'),
    path('adminview/', adminview, name='adminview'),
    path('addview/', addview, name='addview'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
