'use strict';

var app = angular.module('fitApp', [
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
            templateUrl: 'views/mainPage.html'
            // controller: 'AppListCtrl',
        }).
        when('/programs/beginner', {
            templateUrl: 'views/programs/beginner.html'
        }).
        when('/programs/intermediate', {
            templateUrl: 'views/programs/intermediate.html'
        }).
        when('/programs/advanced', {
            templateUrl: 'views/programs/advanced.html'
            // controller: 'LayersCtrl',
        }).      
        // when('/programs/generator', {
        //     templateUrl: 'views/programs/exerciseGenerator.html',
        //     controller: 'ExerciseGeneratorCtrl'
        // }).      
//        when('/programs/nutrition', {
//            templateUrl: 'views/programs/nutrition.html'
//            controller: 'nutritionCtrl'
//        }).
//        when('/contact', {
//            templateUrl: 'views/etc/contact.html',
//            controller: 'contactCtrl'
//        }).  
//        when('/about', {
//            templateUrl: 'views/etc/about.html'
//        }). 
        otherwise({
            redirectTo: '/' 
        });
    } ]
);

