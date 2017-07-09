from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from blog import models as blog_models


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request, **kwargs):
        # Call parent get_context
        context = super(HomePage, self).get_context(request)

        # Query all pages for this site. That are live. Descendant from the homepage, and exclude blog index page types
        # ToDo A better way would be to add a bool field to pages to be included in homepage feed or not
        context['pages'] = Page.objects.in_site(request.site).live().descendant_of(self)\
            .not_type((blog_models.BlogIndexPage,blog_models.BlogTagIndexPage)).order_by('-first_published_at')

        return context
