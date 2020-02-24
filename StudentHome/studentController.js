app.controller("studentCtrl", function($scope) {
    $scope.city = "Select City";
    $scope.state ="Select State";
    $scope.category = "Select Category"; 
    $scope.type ="Select Type";
    
    $scope.agency = function () {
      console.log(window.location.href + "register")
      window.location.href = "file:///D:/Work/Angular%20js/Navbar/home.html#!/" + "student/agency";
  };
  });