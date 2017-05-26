#!/bin/bash

#
# regextester.py
# by Rashaud Teague
##

function regex_posix_bre
{
    local pattern=$1
    local teststr=$2
    return 0
}

function regex_posix_ere
{
    local pattern=$1
    local teststr=$2
    return 0
}

function regex_pcre
{
    local pattern=$1
    local teststr=$2
    return 0
}

function regex_python
{
    local pattern=$1
    local teststr=$2
    local modifiers=$(echo $pattern | grep -oE "^mod:([A-Z]+\|?)+;" | sed -Ee 's/mod:([^;]+);/\1/g')
    pattern=$(echo $pattern | sed -Ee 's/mod:[^;]+;//g')
    
    local flagarg="0"
    if [ "$modifiers" != "" ]; then
        flagarg=$(echo $modifiers | sed -Ee 's/([A-Z]+)/re.\1/g' | sed -Ee 's/\|$//g')
    fi
    
    local scriptcode=$(cat <<END
import re,sys
match = re.match('$pattern', '$teststr', $flagarg)
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
END)
    
    if ! python -c "$scriptcode"; then
        return 1
    fi

    return 0
}

function prog_usage
{
    echo "usage: regextest [-f flavor] pattern teststr"
}

function main
{
    local OPTIND
    
    # $REGXENG is an env variable a user can set with export
    local flavor=${REGXENG:=python}
    
    if [ $# -eq 0 ]; then
        prog_usage
        exit 1
    fi
    
    while getopts ":f:" opt; do
        if [ $opt = "f" ]; then
            flavor=$OPTARG
            if [[ ! "$flavor" =~ ^(bre|ere|pcre|python)$ ]]; then
                prog_usage
                echo "-error: invalid regex flavor selection, (bre,ere,pcre,python; are valid)"
                exit 1
            fi
        fi
    done
    shift $(($OPTIND - 1))
    
    if [ ! $# -eq 2 ]; then
        prog_usage
        exit 1
    fi
    
    case $flavor in
        "bre"    )
            if ! regex_posix_bre "$@"; then
                exit 1
            fi
            ;;
        "ere"    )
            if ! regex_posix_ere "$@"; then
                exit 1
            fi
            ;;
        "pcre"   )
            if ! regex_pcre "$@"; then
                exit 1
            fi
            ;;
        "python" )
            if ! regex_python "$@"; then
                exit 1
            fi
            ;;
    esac

    return 0
}

main "$@"


