app.controller("sideCtrl", function ($scope) {
    $scope.name = "John";
    $scope.path="file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/Navbar/home.html#!/"
    $scope.togg = function () {
        document.getElementById("sidebar").classList.toggle('active')
    }
    
    $scope.search = function () {
        console.log(window.location.href + "register")
        window.location.href = $scope.path + "student/search";
    };

    $scope.logOut = function () {
        console.log(window.location.href + "register")
        window.location.href = $scope.path + "login";
    };

    $scope.home = function () {
        console.log(window.location.href + "register")
        window.location.href = $scope.path + "student/home";
    };
    $scope.studMgmt = function () {
        console.log(window.location.href + "register")
        window.location.href = $scope.path + "student/studMgmt";
    };
});