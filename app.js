'use strict';

var app = angular.module('fitApp', [
    'ngRoute'
 //    'typeAheadModule',
]);

app.config(['$routeProvider', 
    function ($routeProvider) {

        $routeProvider.
        when('/', {
            templateUrl: 'views/mainPage.html'
            // controller: 'AppListCtrl',
        }).
        when('/programs/beginner', {
            templateUrl: 'views/programs/beginner.html'
            // controller: 'LayersCtrl',
        }).
        when('/programs/intermediate', {
            templateUrl: 'views/programs/intermediate.html'
            // controller: 'LayersCtrl',
        }).
        when('/programs/advanced', {
            templateUrl: 'views/programs/advanced.html'
            // controller: 'LayersCtrl',
        }).      
        when('/programs/generator', {
            templateUrl: 'views/programs/exerciseGenerator.html',
            controller: 'ExerciseGeneratorCtrl'
        }).
        when('/progress', {
            templateUrl: 'views/etc/progress.html'
        }).  
        otherwise({
            redirectTo: '/' 
        });
    } ]
);

