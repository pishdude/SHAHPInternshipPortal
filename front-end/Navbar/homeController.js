var app = angular.module("internApp", ['ui.router','ui.bootstrap']);
app.config(function($stateProvider, $urlRouterProvider,$httpProvider) {
    
    $httpProvider.interceptors.push(function() {
        return {
          response: function(res) {
            /* This is the code that transforms the response. `res.data` is the
             * response body */
           // res.data = { data: data };
            //res.data.meta = { status: res.status };
            // console.log("i ma here")
            // console.log(res.status)

            if(res.status == 401){
                alert("Session timed out.Please log back in ")
                window.location.href = "file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/front-end/Navbar/home.html#!/"+ "login";
            }
            return res;
          }
        };
      });

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

app.run(function($http) {
    //editableOptions.theme = 'bs3'; // bootstrap3 theme. Can be also 'bs2', 'default'
    
    var token = window.sessionStorage.getItem('token')
    $http.defaults.headers.common.Authorization = token;
});
app.controller("homeCtrl", function($scope) {
    $scope.firstName = "John";
    $scope.lastName = "Doe";
  });