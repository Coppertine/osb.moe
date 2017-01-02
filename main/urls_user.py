"""
Intended for usage of the user control panel, so all URLs here
should presumably be preceded with something like /user/.
"""

from django.conf.urls import url
from main.views import UserControlPanelHomeView
from main.views import UserControlPanelManageStoryboardView

urlpatterns = [
    url(r'^$', UserControlPanelHomeView.as_view(), name='user_panel_home'),
    url(r'^sb/$', UserControlPanelManageStoryboardView.as_view(), name='user_panel_manage_storyboard')
]