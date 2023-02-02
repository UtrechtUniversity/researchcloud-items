#!/bin/bash

# This is an example script which could be 
# installed in /usr/local/bin on a remote host 
# from which a user intends to transfer data to
# an SRC workspace


if [ -e ~/.ssh/id_rsa ] 
then
	if [ "$1" != '-f' ]
	then
		echo "An existing transfer key exists"
		echo "specify option -f to overwrite that key"
		exit
	fi
	rm ~/.ssh/id_rsa
fi

ssh-keygen -q -f ~/.ssh/id_rsa -N ""
echo "A new transfer key has been generated"
echo "Copy/paste the text below as a key into your ResearchCloud Workspace:"
cat ~/.ssh/id_rsa.pub
