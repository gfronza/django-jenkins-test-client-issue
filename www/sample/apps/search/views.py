# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext


def search(
        request, template_name='search/search.html'):

    return render_to_response(
        template_name, {
            'page': {
                'number': 1,
                'object_list': [{
                    'something': 'test1'
                },
                {
                    'something': 'test2'
                }]
            },
            'paginator': {
                'num_pages': 1
            }
        },
        context_instance=RequestContext(request))
