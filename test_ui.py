#
# '''
# ZetCode wxPython tutorial
#
# In this example, we create a submenu and a menu
# separator.
#
# author: Jan Bodnar
# website: www.zetcode.com
# last modified: September 2011
# '''
#
# import wx
#
#
# def setupPanel(panel):
#     panel.SetBackgroundColour('#00ff00')
#     vbox = wx.BoxSizer(wx.VERTICAL)
#
#     midPan = wx.Panel(panel)
#     midPan.SetBackgroundColour('#00ff00')
#
#     vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
#     panel.SetSizer(vbox)
#
#
# class Example(wx.Frame):
#
#     def __init__(self, *args, **kwargs):
#         super(Example, self).__init__(*args, **kwargs)
#
#         self.InitUI()
#         self.InitBox()
#         self.InitRect()
#
#     def InitUI(self):
#
#         menubar = wx.MenuBar()
#
#         fileMenu = wx.Menu()
#
#
#         imp = wx.Menu()
#         imp.Append(wx.ID_ANY, 'Import game X')
#         imp.Append(wx.ID_ANY, 'Import bookmarks...')
#
#         fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)
#
#         qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
#         fileMenu.AppendItem(qmi)
#
#         self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
#
#         menubar.Append(fileMenu, '&File')
#         self.SetMenuBar(menubar)
#
#
#         self.SetSize((500, 500))
#         self.SetTitle('Deal or No Deal')
#         self.Centre()
#         self.Show(True)
#
#     def InitBox(self):
#         panel = wx.Panel(self)
#         setupPanel(panel)
#
#     def InitRect(self):
#         rect = wx.Rect()
#
#         rect.SetBackgroundColour('#00ff00')
#         vbox = wx.BoxSizer(wx.VERTICAL)
#
#         midPan = wx.Panel(rect)
#         midPan.SetBackgroundColour('#00ff00')
#
#         vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
#         rect.SetSizer(vbox)
#
#
#     def OnMove(self, e):
#
#         x, y = e.GetPosition()
#         self.st1.SetLabel(str(x))
#         self.st2.SetLabel(str(y))
#
#     def OnQuit(self, e):
#         self.Close()
#
# def main():
#
#     ex = wx.App()
#     Example(None)
#     ex.MainLoop()
# #
#
# if __name__ == '__main__':
#     main()

import wx

class MyPanel(wx.Panel):
    """ class MyPanel creates a panel to draw on, inherits wx.Panel """
    def __init__(self, parent, id):
        # create a panel
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour("white")
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, evt):
        """set up the device context (DC) for painting"""
        self.dc = wx.PaintDC(self)
        self.dc.BeginDrawing()
        self.dc.SetPen(wx.Pen("grey",style=wx.TRANSPARENT))
        self.dc.SetBrush(wx.Brush("grey", wx.SOLID))
        # set x, y, w, h for rectangle
        self.dc.DrawRectangle(250,250,50, 50)
        self.dc.EndDrawing()
        del self.dc

app = wx.PySimpleApp()
# create a window/frame, no parent, -1 is default ID
frame = wx.Frame(None, -1, "Drawing A Rectangle...", size = (500, 500))
# call the derived class, -1 is default ID
MyPanel(frame,-1)
# show the frame
frame.Show(True)
# start the event loop
app.MainLoop()