#!/bin/bash
DATA=`date`
echo "content-type: text/plain"
echo
echo  "The date is: $DATA"
# the variable REMOTE_USER indicates a user authenticated by nginx (if present)
echo  "Authenticated User: $REMOTE_USER"
