import wx
from export_archive import export_archive

class DownloaderWindow(wx.Frame):
    def __init__(self):
        super().__init__(parent = None, title="LiveChat Archives Downloader", size=(300,200))
        panel = wx.Panel(self)
        self.token_label = wx.StaticText(panel, pos=(2, 32), label = "Token:")
        self.token_input = wx.TextCtrl(panel, pos=(75,30), size=(200,25))
        self.export_button = wx.Button(panel, pos=(95,115), label="Export Archive")
        self.toke_type_label = wx.StaticText(panel, pos=(2, 62), label = "Token type:")
        self.token_types = ["Basic", "Bearer"]
        self.token_type_choice = wx.Choice(panel, pos=(75, 60), size=(200,25), choices=self.token_types)

        self.export_button.Bind(wx.EVT_BUTTON, self.on_export_button_click)
        
        self.Center()
        self.Show()

    def on_export_button_click(self, event):
        token = self.token_input.GetValue()
        token_type = self.token_type_choice.GetStringSelection()
        export_archive(token, token_type=token_type)


if __name__ == "__main__":
    app = wx.App(False)
    window = DownloaderWindow()
    app.MainLoop()