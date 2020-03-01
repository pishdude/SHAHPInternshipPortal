app.controller("registerCtrl", function($scope) {
    $scope.name = "John";
    $scope.path="file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/Navbar/home.html#!/"
    $scope.validation= function(){
        var forms = document.getElementsByClassName('needs-validation');
        var validation = Array.prototype.filter.call(forms, function (form) {
           
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
           
        });
    }
  });