var app = angular.module('App', []);
app.controller('releasesCtrl', function($scope, $http) {
	$scope.formData = {};
	$scope.releases = [];
	$scope.get = function() {
		$http.get('/api.php?action=get')
			.success(function(data) {
				$scope.releases = data;
			}).error(function(data) {
				alert('Error occurred: ' + data);
			});
	}
	$scope.rowClass = function(rel) {
		switch (rel.state) {
			case '1': return 'warning';
			case '2': return 'success';
			default: return '';
		}
	}
	$scope.processField = function(val) {
		return val ? val : 'N/A';
	}
	$scope.processName = function(rel) {
		if (rel.releaseUrl) {
			return rel.releaseUrl;
		} else if (rel.releasePage) {
			return rel.releasePage;
		} else {
			return null;
		}
	}
	$scope.add = function() {
		$scope.formData['action'] = 'add';
		$http({
			method: 'POST',
			url: '/api.php',
			data: $.param($scope.formData),
			headers: {'Content-Type': 'application/x-www-form-urlencoded'}
		}).success(function(data) {
			if (data == 'OK') {
				alert('Релиз добавлен успешно!');
				$scope.formData['keywords'] = '';
				$scope.get();
			} else {
				alert('Error occured: ' + data);
			}
		}).error(function(data) {
			alert('Error occured: ' + data);
		});
	}
	$scope.remove = function(rid) {
		if (confirm('Хотите удалить этот релиз?')) {
			$http.get('/api.php?action=remove&id=' + rid)
			.success(function(data) {
				if (data == 'OK') {
					alert('Релиз удален успешно!');
					$scope.get();
				} else {
					alert('Error - ' + data);
				}
			})
			.error(function(data) {
				alert('Error occurred: ' + data);
			});
		}
	}
	$scope.get();
});