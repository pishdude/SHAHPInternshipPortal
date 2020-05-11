app.controller("registerCtrl",['$scope', 'loginService','$uibModal',function($scope,loginService,$uibModal) {
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
                $scope.info()
            }, function(error) {
               // $scope.status = 'Unable to insert customer: ' + error.message;
            });
    };


    $scope.info = function (message, student) {
        console.log("hi")
        var modalInstance = $uibModal.open({
          animation: true,
          ariaLabelledBy: 'modal-title',
          ariaDescribedBy: 'modal-body',
          templateUrl: './../Register/model-info.html',
          controller: 'ModalConfirmCtrl',
          controllerAs: 'pc',
          keyboard: false,
          //  size: "lg",
          windowClass: 'show center-modal',
          resolve: {
            data: function () {
              //pc.data = message
              //return pc.data;
            }
          }
        });
    
        modalInstance.result.then(function () {
          window.location.href = $scope.path + "login";
        });
      };

    
  }]);

  app.controller('ModalConfirmCtrl', function ($uibModalInstance, studentService, data, $rootScope) {
    var pc = this;
    pc.data = data;
  
    pc.ok = function () {
     
      $uibModalInstance.close("save");
  
    };
  
    
});