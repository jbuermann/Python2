from django import template

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/
register = template.Library()


# Determine if a page has children
def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent

# @register is a decorator
# inclusion_tag is a method of template.Library(). It is used when a tag renders data using another template
@register.inclusion_tag('tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    # Query the DB for page children that are live and selected to be in the menu
    # This is using wagtail db structure.
    menuitems = parent.get_children().filter(
        live=True,
        show_in_menus=True
    )

    # Set show_dropdown based on if the current item has children or not
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)

    # All of this data will be available in our template
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
