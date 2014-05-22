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
<<<<<<< HEAD
      .when('/dashboard', {
        templateUrl: 'views/dashboard.html',
        controller: 'DashboardCtrl'
=======
      .when('/reservas', {
        templateUrl: 'views/reservas.html',
        controller: 'ReservasCtrl'
>>>>>>> 4dcdef35b0fba6eae7cfbd214f02d00ed45b62ea
      })
      .otherwise({
        redirectTo: '/'
      });
  });
