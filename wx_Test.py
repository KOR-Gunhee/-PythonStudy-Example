import wx

''' UI Setting
class Example(wx.Frame):
    
    def __init__(self, parent, title):
        
        super().__init__(parent, title=title, size=(300, 200))
        
        #self.Move((800, 250))
        self.Centre()
        self.Show()
        
if __name__ == '__main__':
    
    app = wx.App()
    Example(None, title='Center')

app.MainLoop()
'''

#''' Menu Setting
class Menu(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.initui()
        
    def initui(self):
        menubar = wx.MenuBar()
        menu_file = wx.Menu()
        menu_view = wx.Menu()
        
        self.showsb = menu_view.Append(wx.ID_ANY, 'Show Statusbar', 'Toggle Satusbar', kind=wx.ITEM_CHECK)
        self.showtb = menu_view.Append(wx.ID_ANY, 'Show Toolbar', 'Toggle Toolbar', kind=wx.ITEM_CHECK)
        
        menu_view.Check(self.showsb.GetId(), True)
        menu_view.Check(self.showtb.GetId(), True)
        
        self.Bind(wx.EVT_MENU, self.toggle_statusbar, self.showsb)
        self.Bind(wx.EVT_MENU, self.toggle_toolbar, self.showtb)
        
        menubar.Append(menu_file, '&File')
        menubar.Append(menu_view, '&View')
        self.SetMenuBar(menubar)
        
        self.toolbar = self.CreateToolBar()
        self.toolbar.AddTool(1, '', wx.Bitmap('icons/exit.png'))
        self.toolbar.Realize()
        
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')
        
        self.Show(True)
        
    def toggle_statusbar(self, e):
        if self.showsb_IsChecked():
            self.statusbar.Show()
            
        else:
            self.statusbar.Hide()
            
    def toggle_toolbar(self, e):
        if self.Showtb.IsChecked():
            self.toolbar.Show()
            
        else:
            self.toolbar.Hide()

def main():
    app = wx.App()
    Menu(None)
    app.MainLoop()
        
if __name__ == '__main__':
    main()