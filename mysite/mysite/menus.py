from django.core.urlresolvers import reverse
from menu import Menu, MenuItem


# Add two items to our main menu
Menu.add_item("main", MenuItem("Home",
                               '',
                               weight=10,
                               icon="tools"))

# Menu.add_item("main", MenuItem("Blog",
#                                reverse("blog home"),
#                                weight=20,
#                                icon="report"),
#                                children = {
#                                 MenuItem("Articles",
#                                    reverse("articles"),
#                                    weight=20,
#                                    icon="report"),
#                                },)