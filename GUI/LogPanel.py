import wx


class LogPanel(wx.Panel):
    """
    some docstring
    """

    def __init__(self, parent):
        super().__init__(parent=parent)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        self.log = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        layout.Add(self.log, 1, wx.EXPAND, 0)
        self.SetSizer(layout)

    def update(self, actions_text):
        self.log.AppendText(actions_text)
