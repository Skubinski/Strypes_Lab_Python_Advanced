import wx

class BMI(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(BMI, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)

        font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(pnl, label="BMI Calculator", pos=(80, 10))
        heading.SetFont(font)

        self.quantity1 = wx.StaticText(pnl, label="Height: ", pos=(65,80))
        self.quantity2 = wx.StaticText(pnl, label="Weight: ", pos=(65,110))

        self.sc1 = wx.SpinCtrl(pnl, value='0', pos=(115,77), size=(60,-1), max=250)
        self.sc2 = wx.SpinCtrl(pnl, value='0', pos=(115,110), size=(60,-1), max=150)

        calc_btn = wx.Button(pnl, label="Compute", pos=(40, 170))
        calc_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)

        clear_btn = wx.Button(pnl, label="Clear", pos=(140, 170))
        clear_btn.Bind(wx.EVT_BUTTON, self.OnClear)

        self.result = wx.StaticText(pnl, label="", pos=(90, 220))
        self.result.SetFont(font)

        self.desc = wx.StaticText(pnl, label="", pos=(90, 250))
        self.desc.SetFont(font)



        self.SetSize((300, 400))
        self.SetTitle("BMI Calculator")

    def OnCalculate(self, event):
        height = self.sc1.GetValue() / 100
        weight = self.sc2.GetValue()
        bmi = weight / (height ** 2)
        self.result.SetLabel(f"BMI: {bmi:.2f}")
        if bmi < 18.5:
            self.desc.SetLabel("Underweight")
        elif 18.5 <= bmi < 24.9:
            self.desc.SetLabel("Healthy Weight")

        elif 25 <= bmi < 29.9:
            self.desc.SetLabel("Overweight")
        elif bmi >= 30:
            self.desc.SetLabel("Obese")

    def OnClear(self, event):
        self.sc1.SetValue(0)
        self.sc2.SetValue(0)
        self.result.SetLabel("")
        self.desc.SetLabel("")

def main():
    app = wx.App()
    frame = BMI(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()