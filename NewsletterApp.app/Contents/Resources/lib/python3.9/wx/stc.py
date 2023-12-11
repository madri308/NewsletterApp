# This file is generated by wxPython's SIP generator.  Do not edit by hand.
#
# Copyright: (c) 2020 by Total Control Software
# License:   wxWindows License

"""
The :ref:`wx.stc.StyledTextCrtl` class provided by this module is a text widget
primarily intended for use as a syntax highlighting source code editor.  It is
based on the popular Scintilla widget.
"""

from ._stc import *

import wx
ID_ANY = wx.ID_ANY  # Needed for some parameter defaults in this module

EVT_STC_CHANGE = wx.PyEventBinder( wxEVT_STC_CHANGE, 1 )
EVT_STC_STYLENEEDED = wx.PyEventBinder( wxEVT_STC_STYLENEEDED, 1 )
EVT_STC_CHARADDED = wx.PyEventBinder( wxEVT_STC_CHARADDED, 1 )
EVT_STC_SAVEPOINTREACHED = wx.PyEventBinder( wxEVT_STC_SAVEPOINTREACHED, 1 )
EVT_STC_SAVEPOINTLEFT = wx.PyEventBinder( wxEVT_STC_SAVEPOINTLEFT, 1 )
EVT_STC_ROMODIFYATTEMPT = wx.PyEventBinder( wxEVT_STC_ROMODIFYATTEMPT, 1 )
EVT_STC_KEY = wx.PyEventBinder( wxEVT_STC_KEY, 1 )
EVT_STC_DOUBLECLICK = wx.PyEventBinder( wxEVT_STC_DOUBLECLICK, 1 )
EVT_STC_UPDATEUI = wx.PyEventBinder( wxEVT_STC_UPDATEUI, 1 )
EVT_STC_MODIFIED = wx.PyEventBinder( wxEVT_STC_MODIFIED, 1 )
EVT_STC_MACRORECORD = wx.PyEventBinder( wxEVT_STC_MACRORECORD, 1 )
EVT_STC_MARGINCLICK = wx.PyEventBinder( wxEVT_STC_MARGINCLICK, 1 )
EVT_STC_NEEDSHOWN = wx.PyEventBinder( wxEVT_STC_NEEDSHOWN, 1 )
EVT_STC_PAINTED = wx.PyEventBinder( wxEVT_STC_PAINTED, 1 )
EVT_STC_USERLISTSELECTION = wx.PyEventBinder( wxEVT_STC_USERLISTSELECTION, 1 )
EVT_STC_URIDROPPED = wx.PyEventBinder( wxEVT_STC_URIDROPPED, 1 )
EVT_STC_DWELLSTART = wx.PyEventBinder( wxEVT_STC_DWELLSTART, 1 )
EVT_STC_DWELLEND = wx.PyEventBinder( wxEVT_STC_DWELLEND, 1 )
EVT_STC_START_DRAG = wx.PyEventBinder( wxEVT_STC_START_DRAG, 1 )
EVT_STC_DRAG_OVER = wx.PyEventBinder( wxEVT_STC_DRAG_OVER, 1 )
EVT_STC_DO_DROP = wx.PyEventBinder( wxEVT_STC_DO_DROP, 1 )
EVT_STC_ZOOM = wx.PyEventBinder( wxEVT_STC_ZOOM, 1 )
EVT_STC_HOTSPOT_CLICK = wx.PyEventBinder( wxEVT_STC_HOTSPOT_CLICK, 1 )
EVT_STC_HOTSPOT_DCLICK = wx.PyEventBinder( wxEVT_STC_HOTSPOT_DCLICK, 1 )
EVT_STC_HOTSPOT_RELEASE_CLICK = wx.PyEventBinder( wxEVT_STC_HOTSPOT_RELEASE_CLICK, 1 )
EVT_STC_CALLTIP_CLICK = wx.PyEventBinder( wxEVT_STC_CALLTIP_CLICK, 1 )
EVT_STC_AUTOCOMP_SELECTION = wx.PyEventBinder( wxEVT_STC_AUTOCOMP_SELECTION, 1 )
EVT_STC_INDICATOR_CLICK = wx.PyEventBinder( wxEVT_STC_INDICATOR_CLICK, 1 )
EVT_STC_INDICATOR_RELEASE = wx.PyEventBinder( wxEVT_STC_INDICATOR_RELEASE, 1 )
EVT_STC_AUTOCOMP_CANCELLED = wx.PyEventBinder( wxEVT_STC_AUTOCOMP_CANCELLED, 1 )
EVT_STC_AUTOCOMP_CHAR_DELETED = wx.PyEventBinder( wxEVT_STC_AUTOCOMP_CHAR_DELETED, 1 )
EVT_STC_CLIPBOARD_COPY = wx.PyEventBinder( wxEVT_STC_CLIPBOARD_COPY, 1)
EVT_STC_CLIPBOARD_PASTE = wx.PyEventBinder( wxEVT_STC_CLIPBOARD_PASTE, 1)
EVT_STC_AUTOCOMP_COMPLETED = wx.PyEventBinder( wxEVT_STC_AUTOCOMP_COMPLETED, 1)
EVT_STC_MARGIN_RIGHT_CLICK = wx.PyEventBinder( wxEVT_STC_MARGIN_RIGHT_CLICK, 1)
EVT_STC_AUTOCOMP_SELECTION_CHANGE = wx.PyEventBinder( wxEVT_STC_AUTOCOMP_SELECTION_CHANGE, 1)

# compatibility aliases
STC_SCMOD_NORM = STC_KEYMOD_NORM
STC_SCMOD_SHIFT = STC_KEYMOD_SHIFT
STC_SCMOD_CTRL = STC_KEYMOD_CTRL
STC_SCMOD_ALT = STC_KEYMOD_ALT
STC_SCMOD_SUPER = STC_KEYMOD_SUPER
STC_SCMOD_META = STC_KEYMOD_META

