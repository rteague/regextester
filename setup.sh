#!/bin/bash

# setup.sh script template

function installp
{
    if cp ${ex_paths[0]} ${ex_paths[1]} && chmod a+x ${ex_paths[1]}; then
        echo "Installed..."
        return 0
    fi
    return 1
}

function uninstallp
{
    if rm -f ${ex_paths[1]}; then
        echo "Uninstalled..."
    fi
    return 0
}

function prog_usage
{
   echo "usage: bash setup.sh install | uninstall" 
}

function main
{
    # add any other constants or setup variables 
    if [ $# -eq 0 ]; then
        prog_usage
        exit 1
    fi
    
    declare -ra ex_paths=(regext.py /usr/local/bin/regext)
    
    case "$1" in
        "install"   )
            if ! installp; then
                exit 1
            fi
            ;;
        "uninstall" )
            if ! uninstallp; then
                exit 1
            fi
            ;;
        * )
            prog_usage
            exit 1
    esac
    exit 0
}

main "$@"


