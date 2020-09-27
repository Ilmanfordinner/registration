from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from applications import views

urlpatterns = [
    url(r'^applications/(?P<id>[\w-]+)/confirm$', login_required(views.ConfirmApplication.as_view()),
        name='confirm_app'),
    url(r'^applications/(?P<id>[\w-]+)/cancel$', login_required(views.CancelApplication.as_view()),
        name='cancel_app'),
    url(r'^dashboard/$', views.HackerDashboard.as_view(), name='dashboard'),
    url(r'^application/$', views.HackerApplication.as_view(), name='application'),
    url(r'^application/change_to_mentor/$', views.ConvertHackerToMentor.as_view(), name='change_to_mentor'),
    url(r'^application/draft/$', views.save_draft, name='save_draft'),
    url(r'^sponsor/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[\w-]+)/$',
        views.SponsorApplicationView.as_view(), name='sponsor_app'),
    url(r'^sponsor/dashboard/$', views.SponsorDashboard.as_view(), name='sponsor_dashboard'),
]
