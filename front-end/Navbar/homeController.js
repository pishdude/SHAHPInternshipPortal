var app = angular.module("internApp", ['ui.router']);
app.config(function($stateProvider, $urlRouterProvider,$httpProvider) {
    $urlRouterProvider.otherwise('/login');  
    
    $httpProvider.defaults.headers.common = { 
        'Authorization': 'JWT ' + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1ODQwNjM5MTQsInN1YiI6MiwiZXhwIjoxNTg0MjM2NzE5fQ.qDWn7VGRwjkrQ5-P7tQ4W42kbv0VQJn5IUQrPo1ELL8",
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