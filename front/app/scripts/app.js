'use strict';

angular.module('respyManagerApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute'
])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/reservas', {
        templateUrl: 'views/reservas.html',
        controller: 'ReservasCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
