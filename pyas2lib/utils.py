from __future__ import absolute_import
from .compat import StringIO, BytesIO, EmailGenerator
from email import generator as email_generator


def mime_to_string(msg, header_len):
    fp = StringIO()
    g = email_generator.Generator(
        fp, mangle_from_=False, maxheaderlen=header_len)
    g.flatten(msg)
    return fp.getvalue()


def mime_to_bytes(msg, header_len):
    fp = BytesIO()
    g = email_generator.BytesGenerator(
        fp, mangle_from_=False, maxheaderlen=header_len)
    g.flatten(msg)
    return fp.getvalue()

def canonicalize(msg):
    return msg.replace('\r\n', '\n').replace('\r', '\n').replace('\n', '\r\n')
