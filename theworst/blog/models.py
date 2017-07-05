from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

# Wagtail Specific Imports
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index


# Index page for the Blog section (Called Articles in the UI)
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request, **kwargs):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogIndexPage, self).get_context(request)
        context['blogpages'] = self.get_children().live().order_by('-first_published_at')
        return context


# A list of tags to group blog pages together
class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')


# All data we need to compose a Blog Page
class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    content = StreamField([
        ('sub_heading', blocks.CharBlock(classname="sub title")),
        ('paragraph', blocks.RichTextBlock()),
        ('gallery', blocks.ListBlock(
            blocks.StructBlock([
                ('image', ImageChooserBlock()),
                ('caption', blocks.CharBlock())
            ]), template="blog/blocks/carousel.html",
        )),
    ], null=True, blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)


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


