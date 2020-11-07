import wx


class MapPanel(wx.Panel):
    """
    some docstring
    """

    def __init__(self, parent):
        super().__init__(parent=parent)
        layout = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self, label='Map')
        self.textBox = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)

        layout.Add(title, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        layout.Add(self.textBox, 1, wx.EXPAND, 0)

        self.SetSizer(layout)

    def update(self, map_string):
        self.textBox.SetValue(map_string)

    def clear(self):
        self.textBox.SetValue('')
