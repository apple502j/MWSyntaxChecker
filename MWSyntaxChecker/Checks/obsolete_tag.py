"""Check for obsolete tags."""
import re
from MWSyntaxChecker.issueclass import IssueLevel, PageIssue

def del_symbols(text):
    """Remove non-alphabet symbols from string."""
    return ''.join(c for c in text if re.match('^[a-zA-Z]$', c))

def run(text, console=False):
    """Run the check."""
    issueid = 4
    level = IssueLevel.HTML_RULE
    reason = "Never use '{0}' tag since it's obsolete."
    name = 'obsoleteTag'
    issues = []
    tags = [
        'acronym', 'applet', 'basefont', 'bgsound', 'big', 'blink', 'center',
        'command', 'comment', 'dir', 'font', 'frame', 'frameset', 'hgroup',
        'ilayer', 'isindex', 'layer', 'marquee', 'multicol', 'nextid', 'nobr',
        'noembed', 'noframes', 'nolayer', 'plaintext', 'rbc', 'server', 'spacer',
        'strike', 'tt'
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
