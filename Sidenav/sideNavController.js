app.controller("sideCtrl", function ($scope) {
    $scope.name = "John";

    $scope.togg = function () {
        document.getElementById("sidebar").classList.toggle('active')
    }
    
    $scope.search = function () {
        console.log(window.location.href + "register")
        window.location.href = "file:///D:/Work/Angular%20js/Navbar/home.html#!/" + "student/search";
    };

    $scope.logOut = function () {
        console.log(window.location.href + "register")
        window.location.href = "file:///D:/Work/Angular%20js/Navbar/home.html#!/" + "login";
    };

    $scope.home = function () {
        console.log(window.location.href + "register")
        window.location.href = "file:///D:/Work/Angular%20js/Navbar/home.html#!/" + "student/home";
    };
});