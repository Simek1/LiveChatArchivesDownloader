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
        self.status_label = wx.StaticText(panel, pos=(0, 145), label="")

        self.export_button.Bind(wx.EVT_BUTTON, self.on_export_button_click)
        
        self.Center()
        self.Show()

    def on_export_button_click(self, event):
        token = self.token_input.GetValue()
        token_type = self.token_type_choice.GetStringSelection()
        status = export_archive(token, token_type=token_type)
        if status == 200:
            self.status_label.SetLabel("Archive has been exported successfully")
            self.status_label.SetForegroundColour((225, 225, 225))
        else:
            self.status_label.SetLabel(f"Request has failed with status {status}")
            self.status_label.SetForegroundColour((225, 0, 0))
        status_label_size = self.status_label.GetSize()
        status_label_old_pos = self.status_label.GetPosition()
        if status_label_size[0] > 300:
            self.status_label.SetPosition((0, status_label_old_pos[1]))
        else:
            new_x_pos = int((300 - status_label_size[0]) / 2)
            self.status_label.SetPosition((new_x_pos, status_label_old_pos[1]))

if __name__ == "__main__":
    app = wx.App(False)
    window = DownloaderWindow()
    app.MainLoop()