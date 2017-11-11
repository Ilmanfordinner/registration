from app import emails
from app.utils import reverse


def create_reimbursement_email(reimb, request):
    app = reimb.hacker.application
    c = {
        'app': app,
        'reimb': reimb,
        'confirm_url': str(reverse('confirm_app', kwargs={'id': app.uuid_str}, request=request)),
        'form_url': str(reverse('dashboard', request=request)),
        'cancel_url': str(reverse('cancel_app', kwargs={'id': app.uuid_str}, request=request))
    }
    return emails.render_mail('mails/reimbursement',
                              reimb.hacker.email, c)
