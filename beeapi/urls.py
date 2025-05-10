from django.urls import path
from .views import NfdumpView0, NfdumpView1, NfdumpView3, NfdumpView5

urlpatterns = [
    path('nfdump0/', NfdumpView0.as_view(), name='nfdump0'),
    path('nfdump1/', NfdumpView1.as_view(), name='nfdump1'),
    path('nfdump3/', NfdumpView3.as_view(), name='nfdump3'),
    path('nfdump5/', NfdumpView5.as_view(), name='nfdump5'),
]