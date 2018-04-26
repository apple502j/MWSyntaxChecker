"""Check for <br> and blank lines together."""
import re
from MWSyntaxChecker.issueclass import IssueLevel, PageIssue

def run(text, console=False):
    """Run the check."""
    issueid = 1
    level = IssueLevel.CUSTOM
    reason = "Never use both <br> and one blank line."
    name = 'bothBrBlank'
    issues = []
    target = "<br>\n\n"
    iters = re.finditer(target, text)
    for match in iters:
        issues.append(PageIssue(
            issueid,
            name,
            reason,
            level,
            match.start() + 1,
            match.end() + 1
        ))
    if console:
        for istr in map(str, issues):
            print(istr)
    return issues
