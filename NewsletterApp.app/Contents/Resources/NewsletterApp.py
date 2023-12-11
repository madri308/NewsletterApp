from UI import MainFrame, wx

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()