#!/bin/bash

# setup.sh script template

function installp
{
    # add install code
   return 0
}

function uninstallp
{
   # add uninstall code
   return 0
}

function main
{
   # usage report
   declare -r USAGE="usage: bash setup.sh install | uninstall"
   
   # add any other constants or setup variables 
   if [ $# -eq 0 ]; then
      echo $USAGE
      exit 1
    fi
   
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
         echo $USAGE
         exit 1
   esac

   exit 0
}

main "$@"

