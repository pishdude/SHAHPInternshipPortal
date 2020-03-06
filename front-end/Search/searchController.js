app.controller("searchCtrl", ['$scope', 'dataFactory',function($scope,dataFactory) {
 $scope.path="file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/front-end/Navbar/home.html#!/"
    $scope.city = "Select City";
    $scope.state ="Select State";
    $scope.category = "Select Category"; 
    $scope.type ="Select Type";
    getCustomers();

    function getCustomers() {
      var cust = {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1ODMzOTQwMjgsInN1YiI6MSwiZXhwIjoxNTgzNDgwNDMzfQ.CNPfaO6Q6DVHx_5LEoi8pyooCz1PIao5maVEXkAVUCA",
        
      }
        dataFactory.logout(cust)
            .then(function (response) {
                $scope.customers = response.data;
            }, function (error) {
                $scope.status = 'Unable to load customer data: ' + error.message;
            });
    }
    $scope.agency = function () {
      console.log(window.location.href + "register")
      window.location.href = $scope.path + "student/agency";
  };
  }]);