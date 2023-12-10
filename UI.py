import wx
import wx.richtext as rt
import wx.lib.scrolledpanel as scrolled

def new_button(panel, label, event):
    button = wx.Button(panel, label=label)
    button.Bind(wx.EVT_BUTTON, event)
    return button

class RecipientPanel(wx.Panel):
    def __init__(self, parent, to_recipient, cc_recipient, name):
        super(RecipientPanel, self).__init__(parent.recipients_panel)

        self.main_frame = parent

        self.to_recipient = to_recipient
        self.cc_recipient = cc_recipient
        self.name = name

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(self, label=self.name), 0, wx.ALIGN_LEFT)
        sizer.Add(wx.StaticText(self, label=f"  To: {self.to_recipient}"), 0, wx.ALIGN_LEFT,  border=10)
        sizer.Add(wx.StaticText(self, label=f"  CC: {self.cc_recipient}"), 0, wx.ALIGN_LEFT,  border=10)

        send_button = new_button(self, "Send", self.send_mail)
        sizer.Add(send_button, 0, wx.ADJUST_MINSIZE | wx.ALL, border=5)

        open_button = new_button(self, "Open", self.open_mail)
        sizer.Add(open_button, 0, wx.ADJUST_MINSIZE | wx.ALL, border=5)

        self.SetSizer(sizer)

    def send_mail(self, event):
        message = "Are you sure you want to send this mail?"
        caption = "Confirmation"
        style = wx.YES_NO | wx.ICON_QUESTION
        result = wx.MessageBox(message, caption, style)
        if result == wx.YES:
            body_panel_children = self.main_frame.body_panel.GetSizer().GetChildren()
            # IMPLEMENT SEND MAIL FUNCTION

    def open_mail(self, event):
        body_panel_children = self.main_frame.body_panel.GetSizer().GetChildren()

        # IMPLEMENT OPEN MAIL FUNCTION

class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        self.html_content = ""

        # CREATE MAIN PANEL
        self.panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        
        # ========== CREATE DISPLAY PANEL        
        self.window_1 = wx.SplitterWindow(self.panel, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
        display_panel_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Recipients Column
        self.recipients_panel, recipients_sizer = self.create_column("Recipients Groups",  self.window_1)
        display_panel_sizer.Add(self.recipients_panel, 1, wx.EXPAND)

        # IMPLEMENT LOAD DATA
        self.recipients_data = []  # Load data from JSON or initialize an empty list
        self.update_recipients_panel(recipients_sizer)  # Create RecipientPanel instances and add to the recipients column
        
        # Email Column
        self.body_panel, body_sizer = self.create_column("Subject",  self.window_1)

        body_sizer.Add(wx.TextCtrl(self.body_panel), 0, wx.EXPAND, border=5)
        body_sizer.Add((10, 10), 0, wx.EXPAND)
        body_sizer.Add(wx.StaticText(self.body_panel, label="Body"), 0, wx.ALIGN_LEFT)

        body_text = rt.RichTextCtrl(self.body_panel, style=wx.TE_LEFT | wx.TE_MULTILINE | wx.HSCROLL)
        body_sizer.Add(body_text, 1, wx.EXPAND)

        display_panel_sizer.Add(self.body_panel, 5, wx.EXPAND)
        self.window_1.SetSizer(display_panel_sizer)

        self.window_1.SplitVertically(self.recipients_panel, self.body_panel)
        box.Add(self.window_1, 1, wx.EXPAND)
        # ==========

        # ========== BUTTONS PANEL
        self.buttons_panel = wx.Panel(self.panel)
        buttons_panel_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # CREATE BUTTONS AND LABELS
        html_loaded_label = wx.StaticText(self.buttons_panel, label="")
        css_loaded_label = wx.StaticText(self.buttons_panel, label="")

        create_button = new_button(self.buttons_panel, "Create group", self.on_create)
        remove_button = new_button(self.buttons_panel, "Remove group", self.on_remove)
        browse_button = new_button(self.buttons_panel, "Browse mail", lambda event: self.on_browse(body_text, html_loaded_label, css_loaded_label))
        open_button = new_button(self.buttons_panel, "Open HTML", self.open_html_file)

        buttons_panel_sizer.Add(create_button, 0, wx.ADJUST_MINSIZE | wx.ALL, border=5)
        buttons_panel_sizer.Add(remove_button, 0, wx.ADJUST_MINSIZE | wx.ALL, border=5)
        buttons_panel_sizer.Add(browse_button, 0, wx.ADJUST_MINSIZE | wx.ALL, border=5)
        buttons_panel_sizer.Add(open_button, 0, wx.ADJUST_MINSIZE | wx.ALL, border=5)

        buttons_panel_sizer.AddStretchSpacer()

        buttons_panel_sizer.Add(html_loaded_label, 0, wx.EXPAND | wx.ALL, border=5)
        buttons_panel_sizer.Add(css_loaded_label, 0, wx.EXPAND | wx.ALL, border=5)

        self.buttons_panel.SetSizerAndFit(buttons_panel_sizer)
        box.Add(self.buttons_panel, 0, wx.EXPAND)
        # ==========

        self.panel.SetSizerAndFit(box)
        self.SetSize((800, 600))
        self.SetTitle('Newsletter App')
        self.Centre()

    def open_html_file(self, event):
        html_content = self.body_panel.GetSizer().GetChildren()[4].GetWindow().Value

        # IMPLEMENT OPEN FILE

    def create_column(self, label, panel):
        scrolled_panel = scrolled.ScrolledPanel(panel, -1, style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER|wx.ALIGN_LEFT, name="panel1")
        scrolled_panel.SetAutoLayout(1)
        scrolled_panel.SetupScrolling()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(scrolled_panel, label=label), 0, wx.ALIGN_LEFT)
        scrolled_panel.SetSizer(sizer)

        return (scrolled_panel, sizer)

    def on_browse(self, target_text_ctrl, html_loaded_label, css_loaded_label):
        html_wildcard = "HTML files (*.html)|*.html"
        dialog = wx.FileDialog(self, "Choose a file", wildcard=html_wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_OK:
            file_path = dialog.GetPath()
            dialog.Destroy()
            return  
            # IMPLEMENT CREATE AND SHOW HTML
    
    def on_create(self, event):
        # Show a dialog to get user input for new recipient
        dialog = wx.TextEntryDialog(self, 'Enter Name:', 'Create Recipient')
        if dialog.ShowModal() == wx.ID_OK:
            name = dialog.GetValue()
            dialog.Destroy()

            dialog = wx.TextEntryDialog(self, 'Enter To Recipient:', 'Create Recipient')
            if dialog.ShowModal() == wx.ID_OK:
                to_recipient = dialog.GetValue()
                dialog.Destroy()

                dialog = wx.TextEntryDialog(self, 'Enter CC Recipient:', 'Create Recipient')
                if dialog.ShowModal() == wx.ID_OK:
                    cc_recipient = dialog.GetValue()
                    dialog.Destroy()

                    # Add new recipient data and update the recipients panel
                    new_recipient = {"name": name, "to_recipient": to_recipient, "cc_recipient": cc_recipient}
                    self.recipients_data.append(new_recipient)
                    self.update_recipients_panel()

    def on_remove(self, event):
        # Show a dialog to select the recipient to remove
        choices = [data['name'] for data in self.recipients_data]
        dialog = wx.SingleChoiceDialog(self, 'Select recipient to remove:', 'Remove Recipient', choices)
        if dialog.ShowModal() == wx.ID_OK:
            selected_index = dialog.GetSelection()
            dialog.Destroy()

            # Remove the selected recipient data and update the recipients panel
            if selected_index != wx.NOT_FOUND:
                del self.recipients_data[selected_index]
                self.update_recipients_panel()

    def update_recipients_panel(self, recipients_sizer=None):
        recipients_sizer = recipients_sizer or self.recipients_panel.Sizer or wx.BoxSizer(wx.VERTICAL)

        for child in recipients_sizer.GetChildren():
            if (child.GetWindow().ClassName != "wxStaticText"):
                child.GetWindow().Destroy()

        # Create RecipientPanel instances and add to the recipients column
        for recipient_info in self.recipients_data:
            recipient_panel = RecipientPanel(self, recipient_info["to_recipient"], recipient_info["cc_recipient"], recipient_info["name"])
            recipients_sizer.Add(recipient_panel, 0, wx.EXPAND| wx.ALL, border=7)

            # Add a separator between RecipientPanel objects
            separator = wx.StaticLine(self.recipients_panel, style=wx.LI_HORIZONTAL)
            recipients_sizer.Add(separator, 0, wx.EXPAND | wx.ALL, border=3)

        # IMPLEMENT Save data to JSON

        # Refresh the panel
        self.recipients_panel.Layout()