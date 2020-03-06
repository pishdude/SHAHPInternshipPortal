var app = angular.module("internApp", ['ui.router']);
app.config(function($stateProvider, $urlRouterProvider,$httpProvider) {
    $urlRouterProvider.otherwise('/login');  
    
    $httpProvider.defaults.headers.common = { 
        'Authorization': 'JWT ' + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1ODMzOTQwMjgsInN1YiI6MSwiZXhwIjoxNTgzNDgwNDMzfQ.CNPfaO6Q6DVHx_5LEoi8pyooCz1PIao5maVEXkAVUCA",
        'Accept': 'application/json;odata=verbose'
      };
    $stateProvider
        .state('login', {
        url: '/login',
        templateUrl: '../login/login.html'
        })
        .state("register", {
        url: "/register",
        templateUrl: "../Register/register.html"
        })

        .state("student", {
            url: "/student",
            templateUrl: "../SideNav/sidenav.html"
        })
        .state("student.home", {
            url:"/home",
            templateUrl: "../StudentHome/studentHome.html"
        })
        .state("student.studMgmt", {
            url:"/studMgmt",
            templateUrl: "../StudentManagement/studMgmt.html"
        })
        .state("student.search", {
            url:"/search",
            templateUrl: "../Search/search.html"
        })
        .state("student.agency", {
            url:"/agency",
            templateUrl: "../Agency/agency.html"
        });
        

    // $routeProvider
    // .when("/", {
    //     templateUrl : "../login/login.html",
    // })
    // .when("/register", {
    //     templateUrl : "../Register/register.html",
    //     controller : "registerCtrl"
    // })
    // .when("/student", {
    //     templateUrl : "../SideNav/sidenav.html",
    //     controller : "sideCtrl"
    // })
    // .when("/student/search", {
    //     templateUrl : "../Search/search.html",
    //     controller : "searchCtrl"
    // })
    
});
app.controller("homeCtrl", function($scope) {
    $scope.firstName = "John";
    $scope.lastName = "Doe";
  });