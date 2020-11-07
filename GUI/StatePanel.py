import wx


class StatePanel(wx.Panel):
    """
    some docstring
    """

    def __init__(self, parent):
        super().__init__(parent=parent)
        layout = wx.BoxSizer(wx.VERTICAL)

        # create widgets
        self.textBox = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        title = wx.StaticText(self, label='Current Stuff')

        # layout widgets
        layout.Add(title, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        layout.Add(self.textBox, 1, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(layout)

    def update(self, status_text):
        self.textBox.SetValue(status_text)
