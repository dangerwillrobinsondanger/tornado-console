#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
'''
try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO


__all__ = [
    'StringIO',
]
