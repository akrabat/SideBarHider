import sublime, sublime_plugin

PLUGIN_NAME = 'HideSidebarWhenNotFocussed'

class HideSidebarWhenNotFocussedListener(sublime_plugin.EventListener):
  def on_activated(self, view):
    if view.window().is_sidebar_visible():
        # sidebar is visible, so hide it
        view.window().set_sidebar_visible(False)
