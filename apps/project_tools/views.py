from __future__ import absolute_import

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from navigation.widgets import button_navigation_widget

#from .api import tool_items
from . import tool_menu


def tools_list(request):
    context = {
        #'object_list': [button_navigation_widget(request, item) for item in tool_items],
        'object_list': [button_navigation_widget(request, item) for item in tool_menu.getchildren()],
        'title': _(u'tools'),
    }

    return render_to_response('generic_list_horizontal.html', context,
        context_instance=RequestContext(request))
