#!/usr/bin/env casperjs
var casper = require('casper').create({pageSettings: {webSecurityEnabled: false}});
var cp = require('child_process');
var fs = require('fs');
var currentFile = require('system').args[3];

var curFilePath = fs.absolute(currentFile).split('/');
var lastResourceUrl = null;
var captchaSavePath = '/tmp/recaptcha.jpg';

casper.on('resource.requested', function(req) {
	lastResourceUrl = req.url;
});

casper.cli.drop("cli");
casper.cli.drop("casper-path");

var url = casper.cli.get(0);

casper.start(url);

casper.waitForSelector('#download_button', function() {
	casper.click('#download_button');
});

casper.waitUntilVisible('#recaptcha_challenge_image', function() {
	var captcha_url = this.evaluate(function () {
		return document.querySelector('#recaptcha_challenge_image').src;
	});

	if (fs.exists(captchaSavePath)) {
		fs.remove(captchaSavePath);
	}

	this.download(captcha_url, captchaSavePath);

	var code = null;
	if (curFilePath.length > 1) {
		curFilePath.pop();
		fs.changeWorkingDirectory(curFilePath.join('/'));
	}

	cp.execFile('./antigate.sh', ['d70a01bb7ccbfa9869d3ebd71878fe88', captchaSavePath], {}, function(_, stdout, stderr) {
		code = stdout.substring(0, stdout.indexOf('\n'));
	});

	this.waitFor(function check() {
		return code !== null;
	}, function () {
		this.fill('form#recaptcha', {'recaptcha_response_field': code.trim()}, true);
	}, null, 35000);
});

casper.wait(5000, function() {
	this.echo(lastResourceUrl);
});

casper.run();