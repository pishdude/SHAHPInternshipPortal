var app = angular.module("internApp", ['ui.router']);
app.config(function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/login');  
    

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