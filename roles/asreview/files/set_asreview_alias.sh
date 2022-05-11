#!/bin/bash

asreview() {
    if [[ $@ == "lab" ]]; then
        command source /opt/venvs/asreview/bin/activate
        command asreview lab | more
    fi
}
