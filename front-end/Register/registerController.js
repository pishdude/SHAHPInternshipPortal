app.controller("registerCtrl",['$scope', 'dataFactory',function($scope,dataFactory) {
    $scope.path="file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/front-end/Navbar/home.html#!/"
    $scope.validation= function(){
        var forms = document.getElementsByClassName('needs-validation');
        var validation = Array.prototype.filter.call(forms, function (form) {
           
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
                $scope.insertCustomer();
        });
    }

    $scope.name='';
    $scope.ban='';
    $scope.password='';
    $scope.email='';

    $scope.insertCustomer = function () {
        //Fake customer data
        var cust = {
                "username": $scope.name,
                "password":  $scope.password,
                "public_id":  $scope.ban,
                "email":  $scope.email
              }
        dataFactory.insertCustomer(cust)
            .then(function (response) {
                console.log(response)
            }, function(error) {
               // $scope.status = 'Unable to insert customer: ' + error.message;
            });
    };
  }]);