from __future__ import unicode_literals

from django.template import Library

from ..dashboard_widgets import my_favourite_documents, MessageOfTodayItems

register = Library()


@register.simple_tag(takes_context=True)
def user_favourites_items(context):
    return my_favourite_documents(context)


@register.simple_tag()
def motd_marquee():
    return MessageOfTodayItems(template_name="detailed_widgets/detailed_dashboard_widget_motd_marquee.html").as_string()