musicBot
========

scnlog.eu Music Releases watcher bot & downloader (firedrive support, oboom & uploaded via leecher.us).
Supports uploading of unpacked releases to remote host via rsync ssh and notifications via email.

Requirements
============
* python 2.7 (actually used to run the bot itself)
* python-sqlite3 module (database driver used for storing waiting queue)
* python-requests (used to fetch web pages)
* python-lxml (used to parse html)
* python selenium (webdriver api to control phantomjs)
* aria2c (actually used to download files in multi-threading mode)
* unrar (used to unpack archives)
* rsync (used to upload releases to remote storage host)
* fping (used to check if remote storage is alive)
* Mailgun.net active account (to send releases notifications via email)
* ssh access via public key to remote storage
* phantomjs >= 1.9.7 (used to "hack" leecher.us to get direct download link)