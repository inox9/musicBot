var app = angular.module('App', ['ui.bootstrap']);
app.controller('releasesCtrl', function($scope, $http) {
	$scope.formData = {};
	$scope.releases = [];
	$scope.totalItems = 0;
	$scope.currentPage = 1;
	$scope.pageLimit = 12;

	$scope.setPage = function() {
		$scope.get();
	};
	$scope.get = function() {
		var params = {
			action: 'get',
			offset: $scope.pageLimit * ($scope.currentPage - 1),
			limit: $scope.pageLimit
		};
		$http.get('/api.php?' + $.param(params))
			.success(function(data) {
				$scope.releases = data.models;
				$scope.totalItems = data.total;
			}).error(function(data) {
				alert('Error occurred: ' + data);
			});
	};
	$scope.rowClass = function(rel) {
		switch (rel.state) {
			case '1': return 'warning';
			case '2': return 'success';
			default: return '';
		}
	};
	$scope.processField = function(val) {
		return val ? val : 'N/A';
	};
	$scope.processName = function(rel) {
		if (rel.releaseUrl) {
			return rel.releaseUrl;
		} else if (rel.releasePage) {
			return rel.releasePage;
		} else {
			return null;
		}
	};
	$scope.add = function() {
		$scope.formData['action'] = 'add';
		$http({
			method: 'POST',
			url: '/api.php',
			data: $.param($scope.formData),
			headers: {'Content-Type': 'application/x-www-form-urlencoded'}
		}).success(function(data) {
			if (data == 'OK') {
				alert('Запрос добавлен успешно!');
				$scope.currentPage = 1;
				$scope.formData['keywords'] = '';
				$scope.get();
			} else {
				alert('Error occured: ' + data);
			}
		}).error(function(data) {
			alert('Error occured: ' + data);
		});
	};
	$scope.remove = function(rid) {
		if (confirm('Хотите удалить этот запрос из очереди ожидания?')) {
			var params = {action: 'remove', id: rid}
			$http.get('/api.php?' + $.param(params))
			.success(function(data) {
				if (data == 'OK') {
					alert('Запрос удален успешно!');
					$scope.get();
				} else {
					alert('Error - ' + data);
				}
			})
			.error(function(data) {
				alert('Error occurred: ' + data);
			});
		}
	};
	$scope.edit = function(rid, curValue) {
		var newkw = prompt('Пожалуйста, введите новые ключевые слова', curValue);
		if (newkw != null) {
			var params = {action: 'edit', id: rid, newkeywords: newkw}
			$http.get('/api.php?' + $.param(params))
			.success(function(data) {
				if (data == 'OK') {
					alert('Запрос отредактирован!');
					$scope.get();
				} else {
					alert('Error - ' + data);
				}
			})
			.error(function(data) {
				alert('Error occured: ' + data);
			});
		}
	};
	$scope.get();
});