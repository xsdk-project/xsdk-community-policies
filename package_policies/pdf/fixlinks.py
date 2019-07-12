"""
 Convert policy file links to section links in the PDF.
 Also fix image absolute link(s).
"""

import panflute as pf
import re

def action(elem, doc):
    # fix policy links
    if isinstance(elem, pf.Link):
        url = elem.url
        match = re.search('/package_policies/(.+?)\.md', url)
        if match:
            found = match.group(1).lower()
            elem.url = f'#{found}'

    # fix image links with absolute path
    if isinstance(elem, pf.Image):
        url = elem.url
        if url.startswith('/'):
            elem.url = f'../..{url}'

if __name__ == '__main__':
    pf.run_filter(action)

