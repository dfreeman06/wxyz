""" Some widgets
"""
# flake8: noqa
from ._version import __version__, version_info
from .widgets.widget_color import AlphaColorPicker

# these just emulate stuff in lab
from .widgets.widget_dock import DockBox, DockPop
from .widgets.widget_editor import Editor
from .widgets.widget_file import File, FileBox
from .widgets.widget_fullscreen import Fullscreen
from .widgets.widget_svg import SVGBox

# some of these have dependencies that might fail
try:
    from .widgets.widget_json import JSON, JSONPointer, JSONSchema
except ImportError:
    pass

try:
    from .widgets.widget_datagrid import DataGrid
    from .widgets.widget_stylegrid import StyleGrid, CellRenderer, TextRenderer
except ImportError:
    pass

try:
    from .widgets.widget_selectgrid import SelectGrid
except ImportError:
    pass

try:
    from .widgets.widget_jsonld import Expand, Compact, Flatten, Frame, Normalize
except ImportError:
    pass

try:
    from .widgets.widget_markdown import Markdown
except ImportError:
    pass

try:
    from .widgets.widget_template import Template
except ImportError:
    pass

with __import__("importnb").Notebook():
    from .extension import *
