#!/usr/bin/python

#
# regext.py
# by rashaud
# Tue May 30 2017
## 

import re, copy, sys, argparse

class RegexTester(object):
    def __init__(self, lang, flags, expression, teststr):
        self.expression = expression
        self.teststr = teststr
        self.flags = flags # for python
        self.lang = lang
    def test(self):
        if self.lang == 'pcre':
            return self.pcre()
        if self.lang == 'python' or self.lang == 'py':
            return self.python()
    def pcre(self):
        print 'pcre'
        return True
    def python(self):
        flags = re.sub('([a-z])', r"re.\1", self.flags, flags = re.I) if self.flags else self.flags
        matches = re.finditer(self.expression, self.teststr, eval(flags))
        if matches is None:
            print "\033[1;31mMatch failed!\033[m"
            return False
        print "\033[1;32mMatch successful!\033[m"
        for matchno, match in enumerate(matches):
            group_len = len(match.groups())
            print 'Match number %d, with %d group(s):' % (matchno + 1, group_len)
            print 'Full Match = \'%s\'' % match.group()
            for groupno in xrange(0, group_len):
                groupno = groupno + 1
                print 'Group[%s] = \'%s\'' % (groupno, match.group(groupno))
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
    # take stdin or look for files in the cli arguments--after the --expression arg
    data = raw_input() if len(argn.files) == 0 else self.files 
    
    if argn.lang is None:
        parser.print_usage()
        print '%s: error: argument -l/-lang: expects 1 argument' % __file__
        sys.exit(1)
    
    reg = RegexTester(argn.lang, argn.flags, argn.expression[0], data)
    reg.test()

if __name__ == "__main__":
    main()


