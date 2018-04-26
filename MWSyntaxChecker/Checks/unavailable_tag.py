"""Check for tags that do not exist in wikitext."""
import re
from MWSyntaxChecker.issueclass import IssueLevel, PageIssue

def del_symbols(text):
    """Remove all non-alphabet symbols from text."""
    return ''.join(c for c in text if re.match('^[a-zA-Z]$', c))

def run(text, console=False):
    """Run the check."""
    issueid = 5
    level = IssueLevel.MEDIAWIKI_RULE
    reason = "Never use '{0}' tag since it's not available on MediaWiki."
    name = 'unavailableTag'
    issues = []
    tags = [
        'a', 'address', 'area', 'article', 'aside', 'audio',
        'base', 'body', 'button', 'canvas', 'col', 'colgroup',
        'datalist', 'dialog', 'embed', 'fieldset', 'figcaption',
        'figure', 'footer', 'form', 'head', 'header', 'iframe',
        'img', 'input', 'label', 'legend', 'link', 'main', 'map',
        'math', 'menu', 'menuitem', 'meta', 'meter', 'nav',
        'noscript', 'object', 'optgroup', 'option', 'output',
        'param', 'picture', 'progress', 'rtc', 'section', 'select',
        'slot', 'source', 'style', 'summary', 'svg', 'tbody',
        'template', 'textarea', 'tfoot', 'thead', 'track', 'video'
    ]
    tagregexes = []
    for tagname in tags:
        tagregexes.append("<{0} ".format(tagname))
        tagregexes.append("<{0}>".format(tagname))
    for regex in tagregexes:
        iters = re.finditer(regex, text)
        for match in iters:
            issues.append(PageIssue(
                issueid,
                name,
                reason.format(del_symbols(regex)),
                level,
                match.start() + 1,
                match.end() + 1
            ))
    if console:
        for istr in map(str, issues):
            print(istr)
    return issues
