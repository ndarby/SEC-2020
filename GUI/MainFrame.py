import wx
import os
from GUI import MapPanel, LogPanel, StatePanel


class MainFrame(wx.Frame):
    """
    Some docstring
    """
    def __init__(self):
        super(MainFrame, self).__init__(None, title='SEC 2020', size=(600, 400))
        self.CreateStatusBar()

        self.build_gui()
        self.build_menu()

        self.Centre()
        self.Show()

    def build_gui(self):
        """
        some docstring
        """
        main_layout = wx.BoxSizer(wx.VERTICAL)
        mid_layout = wx.BoxSizer(wx.HORIZONTAL)

        # create panels and widgets
        log_dis = LogPanel.LogPanel(self)
        state_dis = StatePanel.StatePanel(self)
        map_dis = MapPanel.MapPanel(self)
        time_dis = wx.StaticText(self, label='Current Time: 0s')

        # arrange panels
        mid_layout.Add(log_dis, 1, wx.EXPAND | wx.ALL, 10)
        mid_layout.Add(map_dis, 3, wx.EXPAND | wx.ALL, 10)

        main_layout.Add(time_dis, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 10)
        main_layout.Add(mid_layout, 10, wx.EXPAND, 0)
        main_layout.Add(state_dis, 10, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(main_layout)

    def build_menu(self):
        """
        some docstring
        """
        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        menu_open = filemenu.Append(1, '&Open\tCtrl-O', 'import a new file')

        self.Bind(wx.EVT_MENU, self.OnLoadFile, menu_open)

        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)

    def run(self):
        pass

    def OnLoadFile(self, event):
        dlg = wx.FileDialog(self, "Please choose a .txt file representing your restaurant.", '', '', '*.txt', wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            path = os.path.join(dirname, filename)
            # pass path to parser

        dlg.Destroy()
