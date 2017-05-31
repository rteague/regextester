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
        if self.lang == 'bre':
            return self.bre()
        if self.lang == 'ere':
            return self.ere()
        if self.lang == 'pcre':
            return self.pcre()
        if self.lang == 'python':
            return self.python()
    def bre(self):
        print 'bre'
    def ere(self):
        print 'ere'
    def pcre(self):
        print 'pcre'
    def python(self):
        flags = re.sub('([a-z])', r"re.\1", self.flags, flags = re.I) if self.flags else self.flags
        match = re.match(self.expression, self.teststr, eval(flags))
        if match is None:
            print "match failed"
            sys.exit()
        i = 0
        print "match successful, matched groups:"
        while True:
            try:
                print "[%d] = %s"  % (i, match.group(i))
            except IndexError, e:
                break
            i = i + 1

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


