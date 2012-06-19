import re


def cdata(text):
    """If you want to fill special chars like & or HTML you have
    to insert a CDATA paragraph.
    """
    if not text:
        return ''
    return "<![CDATA[%s]]>" % text


def make_links_absolute(obj, text):
    """Converts relative links to absolute.
    """
    a_href_re = re.compile(r'<a[^>]*?href="([^"]*)', re.IGNORECASE | re.DOTALL)
    matches = a_href_re.findall(text)
    for m in matches:
        target = obj.restrictedTraverse(m, None)
        if target:
            text = text.replace(
                'href="%s"' % m, 'href="%s"' % target.absolute_url())
    return text


def convert_date(date):
    """Returns the date in format: 2011-2-15 12:55:34
    """
    return '%s %s' % (date.Date().replace('/', '-'),
                      date.Time())


def is_allday(*kw):
    """Checks if all kw (DateTime) .Time() is '00:00:00'.
    """
    for date in kw:
        if date.Time() != '00:00:00':
            return False
    return True
