from django.conf.urls import url

from reimbursement import views

urlpatterns = [
    url(r'^hacker/dash_board/$', views.ReimbursementHacker.as_view(), name='reimbursement_dashboard'),
    url(r'^hacker/review/$', views.ReceiptReview.as_view(), name='receipt_review'),
    url(r'^hacker/send/$', views.SendReimbursementListView.as_view(), name='send_reimbursement'),
    url(r'^hacker/all/$', views.ReimbursementListView.as_view(), name='reimbursement_list'),
    url(r'^hacker/(?P<id>[\w-]+)$', views.ReimbursementDetail.as_view(), name='reimbursement_detail'),
]
