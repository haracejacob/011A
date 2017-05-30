#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 06:27:21 2017

@author: kim
"""
import sys
reload(sys)  
sys.setdefaultencoding('utf8')
import os
from binaryornot.check import is_binary #check if this is binary file or not
import language_check
tool = language_check.LanguageTool('en-US')

#MORFOLOGIK_RULE_EN_US

FIXDIR = './fix/'
ExceptRuleId = ['COMMA_PARENTHESIS_WHITESPACE','WHITESPACE_RULE', 'MORFOLOGIK_RULE_EN_US', 'EN_QUOTES' ,'EN_QUOTES[0]', 'EN_QUOTES[1]', 'EN_QUOTES[2]', 'EN_UNPAIRED_BRACKETS']
def mkdirp(DIRPATH) :
    if not os.path.isdir(DIRPATH) :
	os.makedirs(DIRPATH)

def dirCheck(DIRPATH) :
    dirList = os.listdir(DIRPATH)
    for inFile in dirList :
        if(os.path.isdir(DIRPATH+inFile)) :
	    print(DIRPATH+inFile+'/')
            dirCheck(DIRPATH+inFile+'/')
        elif(is_binary(DIRPATH+inFile)) :
            continue
        else :
            nLine = 0
            f = open(DIRPATH+inFile,'r')
	    TEMPDIR = FIXDIR[:-1]+DIRPATH
	    mkdirp(TEMPDIR)
            fw = open(TEMPDIR+inFile+'.fix','w')
            while True:
                line = f.readline()
                if not line: break
                #matches = tool.check(line.decode('utf-8'))
		                
                matches = tool.check(line)
		for idx in range(len(matches)) :
		    if matches[idx].ruleId in ExceptRuleId :
			continue
                    print DIRPATH+inFile, matches[idx].ruleId
                    data = str(nLine)+' | '+str(matches[idx].fromx)+' '+str(matches[idx].tox)+' | '+line[matches[idx].fromx:matches[idx].tox]+' | '+matches[idx].msg+'\n'
                    print data
                    #fw.write(str(matches[idx]).encode("utf8")+'\n')
		    fw.write(str(matches[idx])+'\n')
		    fw.write(data+'\n')
                   # fw.write(data.encode("utf8")+'\n')
                nLine += 1
            fw.close()
            f.close()

#DIR = './testdir/'
DIR = '/root/workspace/caffe2/'
print DIR
dirCheck(DIR)


