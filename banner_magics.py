#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Jupyter notebook magics (Python 3) to insert Loop banners

Use `%top_banner` and `%bottom_banner`, without backticks, in separate code cells
"""

from IPython.core.magic import register_line_magic
from IPython.display import SVG, Image, HTML

@register_line_magic
def top_banner(line):
    r = Image("loop-struct-header.png")
    display(r)
    hideCode()
    
@register_line_magic
def bottom_banner(line):
    r = Image("loop-struct-foot.png")
    display(r)
    
