from wagtail.contrib.modeladmin.options import (ModelAdmin, ModelAdminGroup, modeladmin_register)
from schedule import admin, models



class Calendar(ModelAdmin):
    model = models.Calendar
    menu_label = 'Create Calendar'  # ditch this to use verbose_name_plural from model


class Events(ModelAdmin):
    model = models.Event
    menu_label = 'Create Events'  # ditch this to use verbose_name_plural from model

class Rules(ModelAdmin):
    model = models.Rule
    menu_label = 'Create Rules'  # ditch this to use verbose_name_plural from model


class MyModelAdminGroup(ModelAdminGroup):
    menu_label = 'Calendar'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (Calendar, Events, Rules)


# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(MyModelAdminGroup)