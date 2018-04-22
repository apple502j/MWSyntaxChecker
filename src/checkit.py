import importlib
import sys
import os
import os.path as path
from checker_settings import CHECK_ISSUES

def checkIt(testName,testText):
    dPath=os.getcwd()
    try:
        os.chdir(path.join(dPath,'Checks'))
        sys.path.append(os.getcwd())
        try:
            test=importlib.import_module(testName)
            test.run(testText,console=True)
            os.chdir(dPath)
        except:
            print("The test '{0}' does not exist.".format(testName))
            os.chdir(dPath)
            return
    except:
        print("The directory 'Checks' does not exist.")
        return
    
def checkAll(testText):
    for check in CHECK_ISSUES:
        checkIt(check,testText)
