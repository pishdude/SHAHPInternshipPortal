app.controller("registerCtrl",['$scope', 'loginService',function($scope,loginService) {
    $scope.path="file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/front-end/Navbar/home.html#!/"
    $scope.validation= function(){
        var forms = document.getElementsByClassName('needs-validation');
        var validation = Array.prototype.filter.call(forms, function (form) {
           
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
                $scope.registerStudent();
        });
    }

    $scope.name='';
    $scope.ban='';
    $scope.password='';
    $scope.email='';
    $scope.interest1 ='';
    $scope.interest2 ='';
    $scope.interest3 ='';

    $scope.registerStudent = function () {
        //Fake customer data
        var cust = {
                "username": $scope.name,
                "name": $scope.name,
                "password":  $scope.password,
                "public_id":  $scope.ban,
                "email":  $scope.email,
                "program": $scope.program,
                "year":$scope.year,
                "bannerId":$scope.ban,
                "interests":  [ $scope.interest1, $scope.interest2, $scope.interest3]
              }
        loginService.insertStudent(cust)
            .then(function (response) {
                console.log(response)
            }, function(error) {
               // $scope.status = 'Unable to insert customer: ' + error.message;
            });
    };
  }]);