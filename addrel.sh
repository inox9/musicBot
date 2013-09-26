#!/bin/bash

if [ $# -ne 1 ]; then
	echo 'wrong argument count'
	exit
fi

sqlite3 /home/pi/mbot/scenerel.db "insert into awaiting(dateadded,keywords,state) values(strftime('%s','now'),'$1',0)"
