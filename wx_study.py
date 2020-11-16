import wx

''' Menu_example
class MyMenu(wx.Frame):
    def __init__(self, parent, id, title):
        
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(200, 150))
        
        menubar=wx.MenuBar()
        
        file=wx.Menu()
        edit=wx.Menu()
        help=wx.Menu()
        
        file.Append(101, '&Open', 'Open a new document')
        file.Append(102, '&Save', 'Save the document')
        file.AppendSeparator()
        
        quit=wx.MenuItem(file, 105, '&Quit\tCtrl+Q', 'Quit the Application')
        quit.SetBitmap(wx.Image('icons/exit.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        
        file.AppendItem(quit)
        
        edit.Append(201, 'check item1', '', wx.ITEM_CHECK)
        edit.Append(202, 'check item2', kind=wx.ITEM_CHECK)
        
        submenu=wx.Menu()
        
        submenu.Append(301, 'radio item1', kind=wx.ITEM_RADIO)
        submenu.Append(302, 'radio item2', kind=wx.ITEM_RADIO)
        submenu.Append(303, 'radio item3', kind=wx.ITEM_RADIO)
        
        edit.AppendMenu(203, 'submenu', submenu)
        
        menubar.Append(file, '&File')
        menubar.Append(edit, '&Edit')
        menubar.Append(help, '&Help')
        
        self.SetMenuBar(menubar)
        self.Center()
        self.Bind(wx.EVT_MENU, self.OnQuit, id=105)
        
        self.CreateStatusBar()
        
    def OnQuit(self, event):
        self.Close()
        
class MyApp(wx.App):
    def OnInit(self):
        
        frame=MyMenu(None, -1, 'menu1.py')
        frame.Center()
        frame.Show(True)
        
        return True
    
app = wx.App()
mainapp = MyApp(app)
mainapp.MainLoop()
'''

''' Toolbar Example
class MyToolBar(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(350, 250))


        vbox = wx.BoxSizer(wx.VERTICAL)

        toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER)

        toolbar.AddSimpleTool(1, wx.Bitmap('icons/new.png'), 'New', '')
        toolbar.AddSimpleTool(2, wx.Bitmap('icons/open.png'), 'Open', '')
        toolbar.AddSimpleTool(3, wx.Bitmap('icons/save.png'), 'Save', '')

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
'''

''' Button Example
class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, (-1, -1), wx.Size(550, 300))
        
        panel = wx.Panel(self, -1)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(wx.Button(panel, -1, 'Button1'), 1, wx.ALL, 5)
        box.Add(wx.Button(panel, -1, 'Button2'), 0, wx.EXPAND)
        box.Add(wx.Button(panel, -1, 'Button3'), 0, wx.ALIGN_CENTER)
        
        panel.SetSizer(box)
        self.Center()
        
        
class MyApp(wx.App):
    def OnInit(self):
        
        frame = MyFrame(None, -1, 'layout.py')
        frame.Show(True)
        return True
    
app = wx.App()
mainapp = MyApp(app)
mainapp.MainLoop()
'''

''' Panel Example
class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        pnl1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        pnl2 = wx.Panel(self, -1, style=wx.RAISED_BORDER)
        pnl3 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        pnl4 = wx.Panel(self, -1, style=wx.NO_BORDER)
        
        hbox.Add(pnl1, 1, wx.EXPAND|wx.ALL, 3)
        hbox.Add(pnl2, 1, wx.EXPAND|wx.ALL, 3)
        hbox.Add(pnl3, 1, wx.EXPAND|wx.ALL, 3)
        hbox.Add(pnl4, 1, wx.EXPAND|wx.ALL, 3)
        
        self.SetSize((400, 120))
        self.SetSizer(hbox)
        self.Center()
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'layout.py')
        frame.Show(True)
        return True
    
app = wx.App()
mainapp = MyApp(app)
mainapp.MainLoop()
'''

''' Grid Example
class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition)
        
        sizer = wx.GridBagSizer(9, 9)
        sizer.Add(wx.Button(self, -1, "Button"), (0, 0), wx.DefaultSpan, wx.ALL, 0)
        sizer.Add(wx.Button(self, -1, "Button"), (1, 1), (1, 7), wx.EXPAND)
        sizer.Add(wx.Button(self, -1, "Button"), (6, 6), (3, 3), wx.EXPAND)
        sizer.Add(wx.Button(self, -1, "Button"), (3, 0), (1, 1), wx.ALIGN_CENTER)
        sizer.Add(wx.Button(self, -1, "Button"), (4, 0), (1, 1), wx.ALIGN_LEFT)
        sizer.Add(wx.Button(self, -1, "Button"), (5, 0), (1, 1), wx.ALIGN_RIGHT)
        sizer.AddGrowableRow(6)
        sizer.AddGrowableCol(6)
        
        self.SetSizerAndFit(sizer)
        self.Centre()
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'Grid.py')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True
    
app = wx.App()
mainapp = MyApp(app)
mainapp.MainLoop()
'''

''' Cursor Example
class Cursors(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        sizer = wx.GridSizer(3, 3, 2, 2)
        
        cursors = [ wx.CURSOR_ARROW, wx.CURSOR_HAND, wx.CURSOR_WATCH, wx.CURSOR_SPRAYCAN, wx.CURSOR_PENCIL,
                   wx.CURSOR_CROSS, wx.CURSOR_QUESTION_ARROW, wx.CURSOR_POINT_LEFT, wx.CURSOR_SIZING]
        
        for i in cursors:
            
            panel = wx.Panel(self, -1, style = wx.SUNKEN_BORDER)
            panel.SetCursor(wx.StockCursor(i))
            sizer.Add(panel, flag = wx.EXPAND)
            
        vbox.Add(sizer, 1, wx.EXPAND|wx.TOP, 5)
        
        self.SetSizer(vbox)
        self.Centre()
        self.Show()
        
app = wx.App()
Cursors(None, -1, 'Cursors.py')
app.MainLoop()
'''

''' Font Example
class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(325, 320))
        
        panel = wx.Panel(self, -1)
        

        text1 = "Hello wxPython Font Test"
        text2 = "Hello wxPython Font Test"
        text3 = "Hello wxPython Font Test"

        font1 = wx.Font(10, wx.SWISS, wx.ITALIC, wx.NORMAL)
        font2 = wx.Font(10, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        font3 = wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD)

        lyrics1 = wx.StaticText(panel, -1, text1, (30, 15), (200, -1), wx.ALIGN_CENTER)
        lyrics1.SetFont(font1)
        lyrics2 = wx.StaticText(panel, -1, text2, (30, 100), (200, -1), wx.ALIGN_CENTER)
        lyrics2.SetFont(font2)
        lyrics3 = wx.StaticText(panel, -1, text3, (5, 220), (200, -1), wx.ALIGN_CENTER)
        lyrics3.SetFont(font3)
        
        
        self.Center()
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'Font.py')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = wx.App()
mainapp = MyApp(app)
mainapp.MainLoop()
'''

''' Color Example
class Colors(wx.Dialog): 
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(300,300))
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.pnl1 = wx.Panel(self, -1)
        self.pnl2 = wx.Panel(self, -1)
        self.pnl3 = wx.Panel(self, -1)
        self.pnl4 = wx.Panel(self, -1)
        self.pnl5 = wx.Panel(self, -1)
        self.pnl6 = wx.Panel(self, -1)
        self.pnl7 = wx.Panel(self, -1)
        self.pnl8 = wx.Panel(self, -1)
        
        gs = wx.GridSizer(4, 2, 3, 3)
        gs.AddMany([(self.pnl1, 0, wx.EXPAND),
                    (self.pnl2, 0, wx.EXPAND),
                    (self.pnl3, 0, wx.EXPAND),
                    (self.pnl4, 0, wx.EXPAND),
                    (self.pnl5, 0, wx.EXPAND),
                    (self.pnl6, 0, wx.EXPAND),
                    (self.pnl7, 0, wx.EXPAND),
                    (self.pnl8, 0, wx.EXPAND)])
                    
        vbox.Add(gs, 1, wx.EXPAND|wx.TOP, 5)
        
        self.SetSizer(vbox)
        self.SetColors()
        self.Centre()
        self.ShowModal()
        self.Destroy()
    
    def SetColors(self):
        self.pnl1.SetBackgroundColour(wx.BLACK)
        self.pnl2.SetBackgroundColour(wx.Colour(139, 105, 20))
        self.pnl3.SetBackgroundColour(wx.RED)
        self.pnl4.SetBackgroundColour('#0000FF')
        self.pnl5.SetBackgroundColour('sea green')
        self.pnl6.SetBackgroundColour('midnight blue')
        self.pnl7.SetBackgroundColour(wx.LIGHT_GREY)
        self.pnl8.SetBackgroundColour('plum')
        
    
app = wx.App(0)
Colors(None, -1, 'colors.py')
app.MainLoop()
'''

''' Timer Example
from random import randrange
from wx.lib.colourdb import *

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(400, 350))
        
        self.panel = wx.Panel(self, -1)
        self.colors = getColourList()
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(500)
        self.col_num = len(self.colors)
        self.Centre()
        
    def OnTimer(self, event):
        self.panel.SetBackgroundColour(wx.RED)
        
        position = randrange(0, self.col_num-1, 1)
        
        self.panel.SetBackgroundColour(self.colors[position])
        self.panel.Refresh()
        
class MyApp(wx.App):
    def OnInit(self):
        updateColourDB()
        frame = MyFrame(None, -1, 'RandomColors.py')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True
    
app = MyApp(0)
app.MainLoop()
'''

''' Bitmap Example
class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (500, 800))
        
        self.bitmap = wx.Bitmap('icons/poster.jpg')
        
        wx.EVT_PAINT(self, self.OnPaint)
        self.Centre()
        
    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bitmap, 60, 20)
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'Bitmap.py')
        frame.Show(True)
        
        self.SetTopWindow(frame)
        return True
    
app = MyApp(0)
app.MainLoop()
'''
        
''' Scroll Event Example
class MyScrollWinEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        
        panel = wx.Panel(self, -1)
        self.st = wx.StaticText(panel, -1, '0', (30, 0))
        panel.Bind(wx.EVT_SCROLLWIN, self.OnScroll)
        panel.SetScrollbar(wx.VERTICAL, 0, 6, 50)
        self.Centre()
        
    def OnScroll(self, evt):
        y = evt.GetPosition()
        self.st.SetLabel(str(y))
        
class MyApp(wx.App):
    def OnInit(self):
        msw = MyScrollWinEvent(None, -1, 'myscrollwinevent.py')
        msw.Show(True)
        return True
    
app = MyApp(0)
app.MainLoop()
'''

'''Size Event Example
class SizeEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Centre()
        
    def OnSize(self, event):
        self.SetTitle(str(event.GetSize()))
        
class MyApp(wx.App):
    def OnInit(self):
        se = SizeEvent(None, -1, 'SizeEvent.py')
        se.Show(True)
        return True
    
app = MyApp(0)
app.MainLoop()
'''

#''' Move Event Example
class MoveEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        
        wx.StaticText(self, -1, 'x:', (10, 0))
        wx.StaticText(self, -1, 'y:', (10, 20))
        self.st1 = wx.StaticText(self, -1, '', (30, 0))
        self.st2 = wx.StaticText(self, -1, '', (30, 20))
        
        self.Bind(wx.EVT_MOVE, self.OnMove)
        self.Centre()
    
    def OnMove(self, event):
        x, y = event.GetPosition()
        
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))
        
class MyApp(wx.App):
    def OnInit(self):
        me = MoveEvent(None, -1, 'MoveEvent.py')
        me.Show(True)
        return True
    
app = MyApp(0)
app.MainLoop()