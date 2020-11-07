import wx


class LogPanel(wx.Panel):
    """
    some docstring
    """

    def __init__(self, parent):
        super().__init__(parent=parent)
        notebook = wx.Notebook(self)
        layout = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self, label='Logs')
        self.mainLog = wx.TextCtrl(notebook, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.robot1Log = wx.TextCtrl(notebook, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.robot2Log = wx.TextCtrl(notebook, style=wx.TE_MULTILINE | wx.TE_READONLY)

        notebook.AddPage(self.mainLog, 'Restaurant')
        notebook.AddPage(self.robot1Log, 'Robot 1')
        notebook.AddPage(self.robot2Log, 'Robot 2')

        layout.Add(title, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        layout.Add(notebook, 1, wx.EXPAND, 0)
        self.SetSizer(layout)

    def update(self, actions_text):
        self.mainLog.AppendText(actions_text)
