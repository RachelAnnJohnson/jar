'use strict';

var app = angular.module('jarApp', [
    'ngRoute',
    'appServices',
    'appFactories',
    'appControllers',
    'appFilters'
]);

app.config(['$routeProvider', 
    function ($routeProvider) {
        $routeProvider.
        when('/', {
            templateUrl: 'views/landing.html'
        }).
        when('/beginner', {
            templateUrl: 'views/programs/beginner.html'
        }).
        when('/intermediate', {
            templateUrl: 'views/programs/intermediate.html'
        }).
        when('/advanced', {
            templateUrl: 'views/programs/advanced.html'
        }).
        otherwise({
            redirectTo: '/' 
        });
    } ]
);