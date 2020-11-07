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
        self.OnLoadFile(None)

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
        actions, state, map_block = self.restaurant.update(self.current_time)
        self.map_dis.update(map_block)
        self.log_dis.update(actions, self.current_time)

        state_text = f"Robot 1: {state['robot1state']}"
        state_text += f", charge: {state['robot1charge']}"
        state_text += f", total distance travelled: {state['robot1distance']}"
        state_text += f", total points: {state['robot1points']}"

        state_text += f"\nRobot 2: {state['robot2state']}"
        state_text += f", charge: {state['robot2charge']}"
        state_text += f", total distance travelled: {state['robot2distance']}"
        state_text += f", total points: {state['robot2points']}"

        self.state_dis.update(state_text)

        self.current_time += 1

    def OnLoadFile(self, event):
        dlg = wx.FileDialog(self, "Please choose a .txt file representing your restaurant.", '', '', '*.txt', wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.state_dis.clear()
            self.log_dis.clear()
            self.map_dis.clear()
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            path = os.path.join(dirname, filename)
            self.restaurant = Restaurant(path)
            self.current_time = 0
            self.updater.Start(1000)

        dlg.Destroy()
