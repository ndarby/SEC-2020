import wx
import os
from GUI import MapPanel, LogPanel, StatePanel
from DataManagement.Restaurant import Restaurant


class MainFrame(wx.Frame):
    """
    Some docstring
    """
    def __init__(self):
        super(MainFrame, self).__init__(None, title='SEC 2020', size=(1200, 800))
        self.CreateStatusBar()

        self.log_dis = None
        self.state_dis = None
        self.map_dis = None
        self.time_dis = None
        self.current_time = 0
        self.restaurant = None

        self.build_gui()
        self.build_menu()

        self.updater = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update)

        self.Centre()
        self.Show()
        #self.test()

    def build_gui(self):
        """
        some docstring
        """
        main_layout = wx.BoxSizer(wx.VERTICAL)
        mid_layout = wx.BoxSizer(wx.HORIZONTAL)

        # create panels and widgets
        self.log_dis = LogPanel.LogPanel(self)
        self.state_dis = StatePanel.StatePanel(self)
        self.map_dis = MapPanel.MapPanel(self)
        self.time_dis = wx.StaticText(self, label='Current Time: 0s')

        # arrange panels
        mid_layout.Add(self.log_dis, 1, wx.EXPAND | wx.ALL, 10)
        mid_layout.Add(self.map_dis, 3, wx.EXPAND | wx.ALL, 10)

        main_layout.Add(self.time_dis, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 10)
        main_layout.Add(mid_layout, 10, wx.EXPAND, 0)
        main_layout.Add(self.state_dis, 5, wx.EXPAND | wx.ALL, 10)

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

    def update(self, e):
        self.time_dis.SetLabel(f'Current Time: {self.current_time}s')
        data = self.restaurant.update(self.current_time)
        print(data)
        self.current_time += 1

    def test(self):
        self.log_dis.update('robot 1 did such and such\n'*500)
        self.map_dis.update("""K 0 0 0 0 0 0 0
0 0 A 4 0 8 0 12
A 0 0 0 0 0 A 0
0 1 0 5 0 9 0 13
0 0 0 0 0 A 0 0
0 2 A 6 0 10 0 14
0 0 0 0 0 0 A 0
0 3 0 7 0 11 0 15
""")

    def OnLoadFile(self, event):
        dlg = wx.FileDialog(self, "Please choose a .txt file representing your restaurant.", '', '', '*.txt', wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            path = os.path.join(dirname, filename)
            self.restaurant = Restaurant(path)
            self.current_time = 0
            self.updater.Start(1000)

        dlg.Destroy()
