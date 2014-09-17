#!/usr/local/bin/casperjs
var casper = require('casper').create();
var system = require('system');
var cp = require('child_process');

casper.lastResourceUrl = null;
casper.captchaSavePath = '/tmp/recaptcha.jpg';

casper.on('resource.requested', function(req) {
	this.lastResourceUrl = req.url;
});

casper.cli.drop("cli");
casper.cli.drop("casper-path");

var url = casper.cli.get(0);

casper.start(url);

casper.waitForSelector('#download_button', function() {
	casper.click('#download_button');
});

casper.waitUntilVisible('#recaptcha_challenge_image', function() {
	this.captureSelector(this.captchaSavePath, '#recaptcha_challenge_image');

	var code = null;
	cp.execFile(__dirname + '/antigate.sh', ['d70a01bb7ccbfa9869d3ebd71878fe88', this.captchaSavePath], {}, function(_, stdout, stderr) {
		code = stdout.substring(0, stdout.indexOf('\n'));
	});

	this.waitFor(function check() {
		return code !== null;
	}, function () {
		this.fill('form#recaptcha', {'recaptcha_response_field': code.trim()}, true);
	}, null, 30000);
});

casper.wait(3500, function() {
	this.echo(this.lastResourceUrl);
});

casper.run();