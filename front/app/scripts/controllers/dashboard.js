'use strict';

angular.module('respyManagerApp')
  .controller('DashboardCtrl', function ($scope, $http) {
		$scope.graphic = "Aqui está um grafico";

    	$http({method : 'GET', url : 'stubs/stub-artefatos.json'})
    	.success(function(data){
    		//console.log(data);
    		$scope.itens = data.item;
    	});
  });
