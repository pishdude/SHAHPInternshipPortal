app.controller("sideCtrl",['$scope', 'loginService',function($scope,loginService) {
    $scope.name = "John";
   $scope.path="file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/front-end/Navbar/home.html#!/"
    $scope.togg = function () {
        document.getElementById("sidebar").classList.toggle('active')
    }
    
    $scope.search = function () {
        console.log(window.location.href + "register")
        window.location.href = $scope.path + "student/search";
    };

    $scope.logOut = function () {
        
        loginService.logout()
            .then(function (response) {
                $scope.customers = response.data;
                window.sessionStorage.clear()
                window.location.href = $scope.path + "login";
                
            }, function (error) {
                $scope.status = 'Unable to load customer data: ' + error.message;
            });
        
    };

    $scope.home = function () {
        console.log(window.location.href + "register")
        window.location.href = $scope.path + "student/home";
    };
    $scope.studMgmt = function () {
        console.log(window.location.href + "register")
        window.location.href = $scope.path + "student/studMgmt";
    };
}]);