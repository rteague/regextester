#!/usr/bin/python

#
# regext.py
# by rashaud
# Tue May 30 2017
## 

import re, os, sys, argparse

class RegexTester(object):
    def __init__(self, lang, flags, expression, teststr):
        self.expression = expression
        self.teststr = teststr
        self.flags = flags # for python
        self.lang = lang
    def test(self):
        if re.match('pcre|perl|php', self.lang):
            return self.pcre()
        if self.lang == 'python' or self.lang == 'py':
            return self.python()
        return False
    def pcre(self):
        perl_code = """
my $text = "%s";
my $matches_found = 0; # boolean
my $matchno = 1; # counter
while ($text =~ %s) {
    if (defined $& && !$matches_found) {
        print "\033[1;32mMatch Successful!\033[m\n";
        $matches_found = 1
    }
    printf("\033[1mMatch number %%d, with %%d group(s):\033[m\n", $matchno, $#-);
    printf("Full Match = '%%s'\n", $&);
    foreach $exp (1..$#-) {
        printf("Group[%%d] = '%%s'\n", $exp, ${$exp});
    }
    $matchno++;
}
if (!$matches_found) {
    print "\033[1;31mMatch failed!\033[m\n";
    exit 1
}
""" % (self.teststr, self.expression)
        if os.system("perl -E '%s'" %  perl_code) != 0:
            return False
        return True
    def python(self):
        flags = re.sub('([a-z])', r"re.\1", self.flags, flags = re.I) if self.flags else self.flags
        matches = re.finditer(self.expression, self.teststr, eval(flags))
        matches_found = False
        for matchno, match in enumerate(matches):
            if not matches_found:
                print '\033[1;32mMatch successful!\033[m'
                matches_found = True
            group_len = len(match.groups())
            print '\033[1mMatch number %d, with %d group(s):\033[m' % (matchno + 1, group_len)
            print 'Full Match = \'%s\'' % match.group()
            for groupno in xrange(0, group_len):
                groupno = groupno + 1
                print 'Group[%s] = \'%s\'' % (groupno, match.group(groupno))
        if not matches_found:
            print '\033[1;31mMatch failed!\033[m'
            return False
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
    if not reg.test():
        sys.exit(1)

if __name__ == "__main__":
    main()


