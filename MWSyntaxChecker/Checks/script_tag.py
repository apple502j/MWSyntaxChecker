"""Check for <script> tags."""
import re
from MWSyntaxChecker.issueclass import IssueLevel, PageIssue

def run(text, console=False):
    """Run the check."""
    issueid = 1
    level = IssueLevel.SECURITY_ISSUE
    reason = "Don't put script tag because it's sometimes dangerous."
    name = 'scriptTag'
    issues = []
    target = "<script"
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
