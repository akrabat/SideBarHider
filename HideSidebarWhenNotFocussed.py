import sublime
import sublime_plugin

PLUGIN_NAME = 'HideSidebarWhenNotFocussed'


class HideSidebarWhenNotFocussedListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        if view:
            if len(view.window().views()) == 0:
                # no open views, so show sidebar
                view.window().set_sidebar_visible(True)
            elif view.window().is_sidebar_visible():
                # sidebar is visible, so hide it
                view.window().set_sidebar_visible(False)
