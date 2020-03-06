app.controller("loginCtrl", function($scope) {
    $scope.name = "John";
   $scope.path="file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/front-end/Navbar/home.html#!/"
    $scope.register = function() {
      console.log(window.location.href+"register")
      window.location.href =$scope.path+"register";
    };
    $scope.login = function () {
      console.log(window.location.href + "register")
      window.location.href = $scope.path + "student/home";
  };
 
  });