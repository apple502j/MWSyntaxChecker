from MWSyntaxChecker import Checks, issueclass

def run_test(test_name,test_text):
  test = getattr(Checks, test_name, None)
  return test.run(test_text)

TESTS = [
    {
        "name":"both_br_blank",
        "text":"Hello! <br>\n\n I like apples.",
        "issueid":"1",
        "issuetype":"bothBrBlank",
        "issuereason":"Never use both <br> and one blank line.",
        "issuelevel":"0",
        "issuestart":"8",
        "issueend":"14"
        
    },
    {
        "name":"obsolete_tag",
        "text":"<center>Welcome to ABC!</center>",
        "issueid":"4",
        "issuetype":"obsoleteTag",
        "issuereason":"Never use 'center' tag since it's obsolete.",
        "issuelevel":"4",
        "issuestart":"1",
        "issueend":"9"
        
    },
]

for t in TESTS:
    result=run_test(t["name"],t["text"])
    if result == issueclass.PageIssue(issue_id=t["issueid"],
        issue_type=t["issuetype"],
        issue_reason=t["issuereason"],
        issue_level=t["issuelevel"],
        issue_start=t["issuestart"],issue_end=t["issueend"]):
        print('Passed:' + t["text"])
    else:
        print('Failed:' + t["text"])
