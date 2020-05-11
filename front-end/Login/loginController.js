app.controller("loginCtrl",['$scope', 'loginService','$http',function($scope,loginService,$http) {
  $scope.email = "";
  $scope.password = "";
  $scope.path = "file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/front-end/Navbar/home.html#!/"

  $scope.validation = function () {
    var forms = document.getElementsByClassName('needs-validation');
    var validation = Array.prototype.filter.call(forms, function (form) {

      if (form.checkValidity() === false) {
        event.preventDefault();
        event.stopPropagation();
      } else {
        $scope.login();
      }
      form.classList.add('was-validated');

    });
  }
  $scope.register = function () {
    console.log(window.location.href + "register")
    window.location.href = $scope.path + "register";
  };


  $scope.login = function () {
    var stud = {
      "password": $scope.password,
      "email": $scope.email
    }
    loginService.login(stud)
      .then(function (response) {
        console.log(response)
        res =response.data
        $http.defaults.headers.common.Authorization = 'jwt ' + res.Authorization;
        window.sessionStorage.setItem("token",'jwt ' + res.Authorization)
        window.location.href = $scope.path + "student/home";
      }, function (error) {
        // $scope.status = 'Unable to insert customer: ' + error.message;
      });
    console.log(window.location.href + "register")
   
  };

}]);