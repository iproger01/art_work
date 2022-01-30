from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm
from .service import send
from .tasks import send_mess_email

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_mess_email.delay(form.instance.email) #delay говорит что для таска
        return super().form_valid(form)

