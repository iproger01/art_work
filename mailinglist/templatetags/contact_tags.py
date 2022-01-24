from django import template
from mailinglist.forms import ContactForm

register = template.Library()

@register.inclusion_tag("malinglist/tags/form.html")
def contact_form():
    return {"contact_form":ContactForm()}