import wx

class MyToolBar(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(350, 250))


        vbox = wx.BoxSizer(wx.VERTICAL)

        toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER)

        toolbar.AddSimpleTool(1, wx.Bitmap('icons/exit.png'), 'New', '')
        toolbar.AddSimpleTool(2, wx.Bitmap('icons/exit.png'), 'Open', '')
        toolbar.AddSimpleTool(3, wx.Bitmap('icons/exit.png'), 'Save', '')

        toolbar.AddSeparator()

        toolbar.AddSimpleTool(4, wx.Bitmap('icons/exit.png'), 'Exit', '')

        tsize = (24, 24)
        toolbar.SetToolBitmapSize(tsize)

        vbox.Add(toolbar, 0,wx.EXPAND)
        toolbar.Realize()       
        self.SetSizer(vbox)
        self.statusbar = self.CreateStatusBar()
        self.Center()
        self.Bind(wx.EVT_TOOL, self.OnNew, id=1)
        self.Bind(wx.EVT_TOOL, self.OnOpen, id=2)
        self.Bind(wx.EVT_TOOL, self.OnSave, id=3)
        self.Bind(wx.EVT_TOOL, self.OnExit, id=4)


    def OnNew(self, event):
        self.statusbar.SetStatusText('New Command')

    def OnOpen(self, event):
        self.statusbar.SetStatusText('Open Command')

    def OnSave(self, event):
        self.statusbar.SetStatusText('Save Command')

    def OnExit(self, event):
        self.Close()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyToolBar(None, -1, 'toolbar.py')
        frame.Show(True)
        return True

app = wx.App()
mainapp = MyApp(app)
app.MainLoop()