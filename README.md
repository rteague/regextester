# RegexTester Template

A CLI tool for testing regular expressions (regex) using various regex languages.

**Table of Contents**

* [Installation/Setup](#installationsetup)
  * [Requirements](#requirements)
* [Usage and Examples](#usage-and-examples)

## Installation/Setup

### Requirements

`regext` was tested on `python version 2.7.10` and it should work with any Unix/Linux system. The embedded perl code was tested on `perl version 5.18.2`.

**Install**

To install system wide run:
```bash
cd /path/to/regextester && sudo bash setup.sh install
```

**Uninstall**

To uninstall the regext program run:
```bash
cd /path/to/regextester && sudo bash setup.sh uninstall
```

## Usage and Examples

Program help:
```bash
regext --help
```

`regext` reads from stdin for the test string, so you could `|` pipe from `echo` or `cat`.

Example 1:
```bash
echo "abcd" | regext -e '/(a(b)c)d/g'
```
Example 1 output:
```bash
Match Successful!
Match number 1, with 2 group(s):
Full Match = abcd
Group[1] = abc
Group[2] = b
```

The default -l/--lang option is `pcre`, you could specify python's regex like so:
```bash
echo "abcd" | regext -l py -e '(a(b)c)d'
```

List of all available regex languages you can run tests with:
* pcre (default) (synonyms: perl, php) 
* python (synonyms: py)

To use python's regex flags use the -f/--flags option after the --lang specification.

For a single flag:
```bash
-f I
```
For multiple flags:
```bash
--flags="I|S"
```

If you expect a lot of output from matches, pipe to `less` with the `-R` option:
```bash
echo "abcd" | regext -l py -f I -e '(a(b)c)d' | less -R
```


