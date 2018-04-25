"""Check for multiple newlines in a row."""
import re
from MWSyntaxChecker.issueclass import IssueLevel, PageIssue

def run(text, console=False):
    """Run the check."""
    issueid = 3
    level = IssueLevel.CUSTOM
    reason = "Don't use too many new lines."
    name = 'tooManyNewLines'
    issues = []
    target = "\n\n\n\n"
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
