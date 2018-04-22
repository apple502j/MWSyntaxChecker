class IssueLevel:
    CUSTOM = 0
    DECIDED_RULE = 1
    DECIDED_STRICT_RULE = 2
    MEDIAWIKI_RULE = 3
    HTML_RULE = 4
    SECURITY_ISSUE = 5

class PageIssue:
    def __init__(self,issueID=0,issueType="",issueReason=None,issueLevel=0,issueStart=0,issueEnd=0):
        self.issueID=issueID
        self.issueType=issueType
        self.issueReason=issueReason
        self.issueLevel=issueLevel
        self.issueStart=issueStart
        self.issueEnd=issueEnd
    def __str__(self):
        return "Issue #{0}:{1} {2} (Level {3}) From {4} To {5}".format(
            self.issueID,
            self.issueType,
            self.issueReason,
            self.issueLevel,
            self.issueStart,
            self.issueEnd,
            )
    def __repr__(self):
        return "<PageIssue issueID='{0}' issueType='{1}' issueReason='{2}' issueLevel='{3}' issueStart='{4}' issueEnd='{5}'>".format(
            self.issueID,
            self.issueType,
            self.issueReason,
            self.issueLevel,
            self.issueStart,
            self.issueEnd,
            )

