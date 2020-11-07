import wx


class StatePanel(wx.Panel):
    """
    some docstring
    """

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.layout = wx.BoxSizer(wx.HORIZONTAL)

        # create widgets
        self.textBox = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)

        # layout widgets
        self.layout.Add(self.textBox, 1, wx.ALL, 20)
