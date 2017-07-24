import sublime
import sublime_plugin

PLUGIN_NAME = 'HideSidebarWhenNotFocussed'


class Vars:
    auto_hide = True


class ToggleSideBarCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        Vars.auto_hide = not Vars.auto_hide
        sublime.active_window().set_sidebar_visible(not Vars.auto_hide)


class HideSidebarWhenNotFocussedListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        if view and Vars.auto_hide:

          
class HideSidebarWhenNotFocussedListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        if view:
            if len(view.window().views()) == 0:
                # no open views, so show sidebar
                view.window().set_sidebar_visible(True)
            elif view.window().is_sidebar_visible():
                # sidebar is visible, so hide it
                view.window().set_sidebar_visible(False)
