"""issue_level and PageIssue classes."""
#pylint: disable=too-few-public-methods
class IssueLevel(object):
    """Constants."""
    CUSTOM = 0
    DECIDED_RULE = 1
    DECIDED_STRICT_RULE = 2
    MEDIAWIKI_RULE = 3
    HTML_RULE = 4
    SECURITY_ISSUE = 5

class PageIssue(object):
    """The page has an issue."""
    #pylint: disable=too-many-arguments
    def __init__(self, issue_id=0, issue_type="", issue_reason=None,
                 issue_level=0, issue_start=0, issue_end=0):
        """Initialize the PageIssue."""
        self.issue_id = issue_id
        self.issue_type = issue_type
        self.issue_reason = issue_reason
        self.issue_level = issue_level
        self.issue_start = issue_start
        self.issue_end = issue_end

    def __str__(self):
        """Stringify self."""
        return "Issue #{0}:{1} {2} (Level {3}) From {4} To {5}".format(
            self.issue_id,
            self.issue_type,
            self.issue_reason,
            self.issue_level,
            self.issue_start,
            self.issue_end,
        )
    def __repr__(self):
        """Represent self."""
        return "<PageIssue issue_id='{0}' issue_type='{1}' issue_reason='{2}' \
issue_level='{3}' issue_start='{4}' issue_end='{5}'>".format(
    self.issue_id,
    self.issue_type,
    self.issue_reason,
    self.issue_level,
    self.issue_start,
    self.issue_end,
)
