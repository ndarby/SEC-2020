import wx
import os
from DataManagement import CSVParser, JSONParser


class MainFrame(wx.Frame):
    """
    Some docstring
    """
    def __init__(self):
        super(MainFrame, self).__init__(None, title='SEC 2020', size=(600, 400))
        self.CreateStatusBar()
        self.layout = wx.BoxSizer(wx.VERTICAL)
        self.data = None

        # create widgets
        self.textBox = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.loadFileButton = wx.Button(self, -1, 'load file')

        # add widgets to layout
        self.layout.Add(self.textBox, 1, wx.ALL | wx.EXPAND, 20)
        self.layout.Add(self.loadFileButton, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 20)

        # add functionality to widgets
        self.Bind(wx.EVT_BUTTON, self.OnLoadFile, self.loadFileButton)

        self.SetSizer(self.layout)
        self.Centre()
        self.Show()

    def OnLoadFile(self, event):
        dlg = wx.FileDialog(self, "Choose a file", '', '', 'CSV files (*.csv)|*.csv|JSON files (*.json)|*.json', wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            if '.json' in filename:
                self.data = JSONParser.parse(os.path.join(dirname, filename))
            elif '.csv' in filename:
                self.data = CSVParser.parse(os.path.join(dirname, filename))
            self.textBox.SetValue(str(self.data))

        dlg.Destroy()
