import wx
import wx.adv

mode = "dark"
animal = "cat"

class RunningCat(wx.adv.TaskBarIcon):
    currentImage = -1
    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(50)
    
    def OnTimer(self, evt):
        self.currentImage = (self.currentImage + 1) % 5
        self.SetIcon(wx.Icon(animal + "/" + mode + "_" + animal + "_"
                            + str(self.currentImage) + ".ico"))

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None)
        self.taskBarIcon = RunningCat()

app = wx.App()
frm = MyFrame()
app.MainLoop()
