#!/bin/bash

DBPATH = /home/pi/mbot/scenerel.db

if [ $# -ne 1 ]; then
	echo 'wrong argument count'
	exit
fi

sqlite3 $DBPATH "insert into awaiting(dateadded,keywords,state) values(strftime('%s','now'),'$1',0)"
