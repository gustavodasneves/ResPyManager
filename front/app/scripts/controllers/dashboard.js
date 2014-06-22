'use strict';

angular.module('respyManagerApp')
  .controller('DashboardCtrl', function ($scope, $http, Appfacade) {
		$scope.graphic = "Gráfico";

    	$http({method : 'GET', url : Appfacade.mountUri('equipamentos') })
    	.success(function(data){
    		console.log(appfacade.uri);
    		$scope.itens = data.item;
    	});
  });
