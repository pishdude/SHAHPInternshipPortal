app.controller("studMgmtCtrl", function($scope) {
   $scope.path="file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/front-end/Navbar/home.html#!/"

    $scope.searchType =false;

    $scope.agency = function () {
      console.log(window.location.href + "register")
      window.location.href = $scope.path + "student/agency";
  };

    $scope.typeChange=function(){
      
      console.log("type="+$scope.searchType)
      
    }

    
  });
  