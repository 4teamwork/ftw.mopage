import re
from DateTime import DateTime


def cdata(text):
    """ Wrap text into a cdata tag.

    Used when putting html into a xml tag
    """
    if not text:
        return ''
    return "<![CDATA[%s]]>" % text


def make_links_absolute(obj, text):
    """ Search for links into text and convert them into
    absolute links.

    obj is used to search the objects the links are referring to.
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
    """ Returns the date in format: 2011-02-15 12:55:34
    """

    if not isinstance(date, DateTime):
        return date

    return '%s %s' % (date.Date().replace('/', '-'),
                      date.Time())


def is_allday(*dates):
    """ Look for all dates's time. If them all are 00:00:00, it is a allday
    """
    for date in dates:
        if not isinstance(date, DateTime):
            continue

        if date.Time() != '00:00:00':
            return False
    return True
