# Common Script to load "issueclass"
from importlib import import_module as import2
from os.path import split as psplit
from os import getcwd,chdir
import re
dpath=getcwd()
chdir(psplit(dpath)[0])
global issueclass, IssueLevel, PageIssue
issueclass=import2('issueclass')
IssueLevel=issueclass.IssueLevel
PageIssue=issueclass.PageIssue
chdir(dpath)

def run(t,console=False):
    # Settings
    global IssueLevel, PageIssue
    iid=1
    lv=IssueLevel.SECURITY_ISSUE
    r="Don't put script tag because it's sometimes dangerous."
    n='scriptTag' 
    issues=[]
    target="<script"
    iters=re.finditer(target,t)
    for match in iters:
        issues.append(PageIssue(iid,n,r,lv,match.start()+1,match.end()+1))
    if console:
        for istr in list(map(str,issues)):
            print(istr)
    return issues
