"""Check for non-bracket category links."""
import re
from MWSyntaxChecker.issueclass import IssueLevel, PageIssue

def run(text, console=False):
    """Run the check."""
    issueid = 2
    level = IssueLevel.MEDIAWIKI_RULE
    reason = "Use [[Category:Category]] instead of {{Category:Category}}."
    name = 'useBracketForCategory'
    issues = []
    target = r"\{\{([cC]ategory|カテゴリ):"
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
