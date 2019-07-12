"""
 Convert policy file links to section links in the PDF.
"""

import panflute as pf
import re

def action(elem, doc):
    if isinstance(elem, pf.Link):
        url = elem.url
        match = re.search('/package_policies/(.+?)\.md', url)
        if match:
            # fix policy links
            found = match.group(1).lower()
            elem.url = f'#{found}'

if __name__ == '__main__':
    pf.run_filter(action)

