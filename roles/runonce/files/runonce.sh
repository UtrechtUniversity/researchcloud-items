#!/bin/bash
# /etc/profile.d/runonce
# Aug2021/TSM
#
# This script will execute, only once, a set of scripts for a new Linux user (upon login)
# The target scripts (must be executable) should be placed
# in (a subdir of) directory /etc/runonce.d 
#
# NB: the target scripts are executed in the current shell.
#
# requires interactive bash/zsh shell
if [ -h ~/runonce.d -a -d /etc/runonce.d -a -n "$PS1" ] && [ -n "$BASH_VERSION" -o -n "$ZSH_VERSION"] ]; then
	for i in `find -L ~/runonce.d -type f -a -executable -print|sort`
	do
		echo "--- Runonce: executing $i"
		. $i
	done;
	rm ~/runonce.d
fi
