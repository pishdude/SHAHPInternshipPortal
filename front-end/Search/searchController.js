app.controller("searchCtrl", ['$scope' ,function() {
 $scope.path="file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/front-end/Navbar/home.html#!/"
    $scope.city = "Select City";
    $scope.state ="Select State";
    $scope.category = "Select Category"; 
    $scope.type ="Select Type";
    getCustomers();

    function getCustomers() {
     
    }
    $scope.agency = function () {
      console.log(window.location.href + "register")
      window.location.href = $scope.path + "student/agency";
  };
  }]);