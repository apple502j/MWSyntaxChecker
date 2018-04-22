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

def delSymbols(t):
    chars=[]
    for char in t:
        if re.match("^[a-zA-Z]$",char):
            chars.append(char)
    return ''.join(chars)

def run(t,console=False):
    # Settings
    global IssueLevel, PageIssue
    iid=5
    lv=IssueLevel.MEDIAWIKI_RULE
    r="Never use '{0}' tag since it's not available on MediaWiki."
    n='unavailableTag'
    issues=[]
    tags=['a','address','area','article','aside','audio',
          'base','body','button','canvas','col','colgroup',
          'datalist','dialog','embed','fieldset','figcaption',
          'figure','footer','form','head','header','iframe',
          'img','input','label','legend','link','main','map',
          'math','menu','menuitem','meta','meter','nav',
          'noscript','object','optgroup','option','output',
          'param','picture','progress','rtc','section','select',
          'slot','source','style','summary','svg','tbody',
          'template','textarea','tfoot','thead','track','video']
    tagregexes=[]
    for tagname in tags:
        tagregexes.append("<{0} ".format(tagname))
        tagregexes.append("<{0}>".format(tagname))
    for regex in tagregexes:
        iters=re.finditer(regex,t)
        for match in iters:
            issues.append(PageIssue(iid,n,r.format(delSymbols(regex)),lv,match.start()+1,match.end()+1))
    if console:
        for istr in list(map(str,issues)):
            print(istr)
    return issues
