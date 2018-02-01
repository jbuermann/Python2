from django.db import models
from django import forms
from django.utils import timezone
from wagtailmenus.models import MenuPage

from modelcluster.fields import ParentalKey,ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

# Wagtail Specific Imports
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

COMMON_BLOCKS = [
    ('sub_heading', blocks.CharBlock(classname="sub title")),
    ('paragraph', blocks.RichTextBlock()),
    ('gallery', blocks.ListBlock(
        blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('caption', blocks.CharBlock())
        ]), template="blog/blocks/carousel.html",
    ))
]


# Index page for the Blog section (Called Articles in the UI)
class BlogIndexPage(MenuPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request, **kwargs):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogIndexPage, self).get_context(request)
        context['blogpages'] = self.get_children().live().order_by('-first_published_at')
        return context


# A list of tags to group blog pages together
class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')


# All data we need to compose a Blog Page
class BlogPage(MenuPage):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    content = StreamField(COMMON_BLOCKS, null=True, blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('content'),
    ]

    # Add fields to the admin page, content panels also add UI
    # MultiFieldPanel combines a group of fields
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            ImageChooserPanel('cover'),
        ], heading="Blog information"),
        FieldPanel('intro'),
        StreamFieldPanel('content'),
    ]


# Create a page - display pages grouped by custom Tags
# This model just allows us to hit the DB for data when get_context is called
# You do need to create this page type in Admin
class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super(BlogTagIndexPage, self).get_context(request)
        context['blogpages'] = blogpages
        return context


#
# EVENTS
#
class EventIndexPage(MenuPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request, **kwargs):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(EventIndexPage, self).get_context(request)
        context['events'] = self.get_children().live().order_by('-first_published_at')
        context['today'] = timezone.now()
        return context


# All data we need to compose an Event Page
class EventPage(MenuPage):
    start = models.DateTimeField("Start date")
    end = models.DateTimeField("End date")
    intro = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250, null=True, blank=True)
    content = StreamField(COMMON_BLOCKS, null=True, blank=True)
    banner = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    vue = models.ForeignKey('blog.VueComps', on_delete=models.SET_NULL, null=True, related_name='+')

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('content'),
    ]

    # Add fields to the admin page, content panels also add UI
    # MultiFieldPanel combines a group of fields
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('start'),
            FieldPanel('end'),
            FieldPanel('location'),
            FieldPanel('facebook'),
            ImageChooserPanel('banner'),
            ImageChooserPanel('cover'),
        ], heading="Event Information"),
        FieldPanel('intro'),
        StreamFieldPanel('content'),
        SnippetChooserPanel('vue'),
    ]


@register_snippet
class VueComps(models.Model):
    title = models.CharField(max_length=255)
    markup = StreamField([('vue',blocks.RawHTMLBlock(required=False))], null=True, blank=True)
    panels = [
        FieldPanel('title'),
        StreamFieldPanel('markup'),
    ]

    def __str__(self):
        return self.title