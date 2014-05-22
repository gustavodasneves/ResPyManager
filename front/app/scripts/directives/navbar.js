'use strict';

angular.module('respyManagerApp')
  .directive('navbar', function () {
    return {
      templateUrl: 'views/templates/navbar.html',
      restrict: 'E',
      link: function postLink(scope, element, attrs) {
      }
    };
  });
