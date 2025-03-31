import wx
from export_archive import export_archive

class DownloaderWindow(wx.Frame):
    def __init__(self):
        super().__init__(parent = None, title="LiveChat Archives Downloader", size=(300,200))
        panel = wx.Panel(self)
        self.token_input = wx.TextCtrl(panel, pos=(50,30), size=(200,25))
        self.export_button = wx.Button(panel, pos=(95,80), label="Export Archive")

        self.export_button.Bind(wx.EVT_BUTTON, self.on_export_button_click)
        
        self.Center()
        self.Show()

    def on_export_button_click(self, event):
        token = self.token_input.GetValue()
        export_archive(token)


if __name__ == "__main__":
    app = wx.App(False)
    window = DownloaderWindow()
    app.MainLoop()