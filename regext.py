#!/usr/bin/python

#
# regext.py
# by rashaud
# Tue May 30 2017
## 

import re, sys, argparse

class RegexTester(object):
    def __init__(self, lang, flags, expression, teststr):
        self.expression = expression
        self.teststr = teststr
        self.flags = flags # for python
        self.lang = lang
    def test(self):
        if self.lang == 'pcre':
            return self.pcre()
        if self.lang == 'python':
            return self.python()
    def pcre(self):
        print 'pcre'
        return True
    def python(self):
        flags = re.sub('([a-z])', r"re.\1", self.flags, flags = re.I) if self.flags else self.flags
        matches = re.findall(self.expression, self.teststr, eval(flags))
        matches_len = len(matches)
        if matches_len == 0:
            print "Match failed!"
            return False
        print "Match successful! matches and their groups:"
        for matchno, match in enumerate(matches):
            matchno = matchno + 1
            print 'Match number %d:' % matchno
            if type(match) == str:
                print 'Full match, Group[1] = \'%s\'' % match
            else:
                for groupno, group in enumerate(match):
                    if groupno == 0:
                        print 'Full match, Group[%s] = \'%s\'' % (groupno + 1, group)
                    else:
                        print 'Group[%s] = \'%s\'' % (groupno + 1, group)
        return True

def main():
    class arg_namespace():pass
    argn = arg_namespace()
    parser = argparse.ArgumentParser(
        description = 'A CLI tool for testing regular expressions (regex) using various regex langs (bre, ere, pcre, etc.).',
        epilog = 'by Rashaud Teague'
    )
    parser.add_argument('-l', '--lang', nargs = '?', default = 'pcre')
    parser.add_argument('-m', '--flags', nargs = '?', default = '0', help = '-m I or --flags="I|S|U"')
    parser.add_argument('-e', '--expression', nargs = 1, type = str, required = True)
    parser.add_argument('files', nargs = '*')
    parser.parse_args(namespace = argn)
    # process
    data = raw_input() if len(argn.files) == 0 else self.files 
    reg = RegexTester(argn.lang, argn.flags, argn.expression[0], data)
    reg.test()

if __name__ == "__main__":
    main()


