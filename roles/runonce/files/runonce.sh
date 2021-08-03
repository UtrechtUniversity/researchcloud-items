#!/bin/bash
# /etc/profile.d/runonce
# Aug2021/TSM
#
# This script will execute, only once, a set of bash scripts for a new Linux user (upon login)
# The target scripts should be placed in directory /etc/skel/runonce.d 
#
# requires interactive bash/zsh shell
if [ -h ~/runonce.d -a -d /etc/runonce.d -a -n "$PS1" ] && [ -n "$BASH_VERSION" -o -n "$ZSH_VERSION"] ]; then
	# show date so that user can review how long configuration activity has taken
	echo "Please stand by while your environment is configured"
	echo "(executing scripts copied from /etc/skel/runonce.d)"
	echo "Started configuration at: `date`"
	source ~/runonce.d/*
	echo "Finished configuration at: `date`"
	rm ~/runonce.d
fi
