#!/bin/bash

systemctl enable apt-daily.timer
systemctl enable apt-daily-upgrade.timer
systemctl start apt-daily.timer
systemctl start apt-daily-upgrade.timer

systemctl stop upgrade-bootstrap.timer
systemctl disable upgrade-bootstrap.timer