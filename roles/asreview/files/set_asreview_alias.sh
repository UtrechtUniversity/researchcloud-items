#!/bin/bash

asreview() {
    if [[ $@ == "lab" ]]; then
        command source /opt/venvs/asreview/bin/activate && asreview lab | more
    fi
}
