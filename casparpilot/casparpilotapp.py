from kivy.app import App
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image


class CasparPilotApp(App):
    """Basic kivy app

    Edit casparpilot.kv to get started.
    """

    def build_config(self, config):
        config.setdefaults('caspar_server', {
            'host': 'localhost',
            'port': '5250'
        })

    def build_settings(self, settings):
        jsondata = """
[
    { "type": "string",
      "title": "Hostname",
      "desc": "Description of my first key",
      "section": "caspar_server",
      "key": "host" },

    { "type": "numeric",
      "title": "Port",
      "desc": "Description of my second key",
      "section": "caspar_server",
      "key": "port" }
]
"""
        settings.add_json_panel('CasparCG Server Settings',
            self.config, data=jsondata)

    def build(self):
        tab_panel= TabbedPanel()
        tab_panel.do_default_tab = False
        tab_panel.tab_width = 150
        tab_panel.tab_height = 30

        th_playlist = TabbedPanelHeader(text='Playlist Playout')
        th_playlist.content = Label(text='UI to create a playlist rundown')

        th_generic_live = TabbedPanelHeader(text='Generic Live Event')
        th_generic_live.content = Label(text='UI for running random live events')

        th_news = TabbedPanelHeader(text='News Broadcast')
        th_news.content = Label(text='UI for running a live news broadcast')

        th_worship = TabbedPanelHeader(text='Worship')
        th_worship.content= Label(text='UI for running praise & worships')

        th_football = TabbedPanelHeader(text='Football')
        th_football.content= Label(text='UI for running a football match')

        th_volleyball = TabbedPanelHeader(text='Volleyball')
        th_volleyball.content= Label(text='UI for running a volleyball match')

        tab_panel.add_widget(th_playlist)
        tab_panel.add_widget(th_generic_live)
        tab_panel.add_widget(th_news)
        tab_panel.add_widget(th_worship)
        tab_panel.add_widget(th_football)
        tab_panel.add_widget(th_volleyball)

        tab_panel.default_tab = th_playlist

        return tab_panel

