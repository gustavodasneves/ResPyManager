'use strict';

angular.module('respyManagerApp')
  .directive('footer', function () {
    return {
      templateUrl: 'views/templates/footer.html',
      restrict: 'E',
      link: function postLink(scope, element, attrs) {
       }
    };
  });
