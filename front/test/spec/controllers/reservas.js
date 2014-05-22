'use strict';

describe('Controller: ReservasCtrl', function () {

  // load the controller's module
  beforeEach(module('respyManagerApp'));

  var ReservasCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ReservasCtrl = $controller('ReservasCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
