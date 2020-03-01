app.controller("studentCtrl", function($scope) {
  $scope.path="file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/Navbar/home.html#!/";
    $scope.city = "Select City";
    $scope.state ="Select State";
    $scope.category = "Select Category"; 
    $scope.type ="Select Type";
    
    $scope.agency = function () {
      console.log(window.location.href + "register")
      window.location.href = $scope.path + "student/agency";
  };
  });