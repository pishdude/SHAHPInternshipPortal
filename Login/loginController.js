app.controller("loginCtrl", function($scope) {
    $scope.name = "John";

    $scope.register = function() {
      console.log(window.location.href+"register")
      window.location.href ="file:///D:/Work/Angular%20js/Navbar/home.html#!/"+"register";
    };
    $scope.login = function () {
      console.log(window.location.href + "register")
      window.location.href = "file:///D:/Work/Angular%20js/Navbar/home.html#!/" + "student/home";
  };
 
  });