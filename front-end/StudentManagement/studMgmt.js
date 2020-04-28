app.controller("studMgmtCtrl", ['$rootScope', '$scope', 'studentService', '$uibModal', function ($rootScope, $scope, studentService, $uibModal) {
  $scope.path = "file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/front-end/Navbar/home.html#!/"
  var pc = this;
  pc.data = "Lorem Name Test";
  $scope.searchValue = ''
  $scope.searchType = false;
  $scope.students
  $scope.alerts = []
  $scope.totalItems = 64;
  $scope.currentPage = 1;
  $scope.maxSize = 5;
  $scope.itemsPerPage = 1;
  $rootScope.currentPage2 = 1
 
  
  $scope.pageChanged = function () {
    
      $rootScope.getStudents($scope.currentPage)
      $rootScope.currentPage2 = $scope.currentPage
      console.log('Page changed to: ' + $scope.currentPage);
   
  };

  
  $rootScope.getStudents = function (page) {
    studentService.searchStudents($scope.searchValue, $scope.searchType,page).then(function (response) {
      console.log(response)
      $scope.students = response.data.data
      if($scope.students[0])
      $scope.totalItems = $scope.students[0].count;
      else
      $scope.totalItems = 0
      console.log($scope.students[0])

    }, function (error) {
      // $scope.status = 'Unable to insert customer: ' + error.message;
    });
  }
  $rootScope.getStudents(1)

  $scope.show = function (student) {
    console.log("hi")
    var modalInstance = $uibModal.open({
      animation: true,
      ariaLabelledBy: 'modal-title',
      ariaDescribedBy: 'modal-body',
      templateUrl: './../StudentManagement/model-form.html',
      controller: 'ModalInstanceCtrl',
      controllerAs: 'pc',
      keyboard: false,
      size: "lg",
      windowClass: 'show center-modal',
      resolve: {
        data: function () {
          pc.data = student
          return pc.data;
        }
      }
    });

    modalInstance.result.then(function () {
      // alert("now I'll close the modal");
      //$rootScope.getStudents($scope.currentPage)
      $scope.alerts.push({ type: 'success', msg: 'Another alert!' });

    });
  };

  $scope.closeAlert = function (index) {
    $scope.alerts.splice(0);
  };

  $scope.activate = function (student) {
    let body = {
      'email': student.email
    }
    studentService.activateStudent(body).then(function (response) {
      console.log(response)
      $rootScope.getStudents($rootScope.currentPage2)


    }, function (error) {
      // $scope.status = 'Unable to insert customer: ' + error.message;
    });
  }

  $scope.confirm = function (message, student) {
    console.log("hi")
    var modalInstance = $uibModal.open({
      animation: true,
      ariaLabelledBy: 'modal-title',
      ariaDescribedBy: 'modal-body',
      templateUrl: './../StudentManagement/model-confirm.html',
      controller: 'ModalConfirmCtrl',
      controllerAs: 'pc',
      keyboard: false,
      //  size: "lg",
      windowClass: 'show center-modal',
      resolve: {
        data: function () {
          pc.data = message
          return pc.data;
        }
      }
    });

    modalInstance.result.then(function () {
      if (message == 'activate/deactivate') {
        $scope.activate(student)
      }

    });
  };

}]);

app.controller('ModalInstanceCtrl', function ($uibModalInstance, studentService, data, $rootScope) {
  var pc = this;
  pc.data = data;
  student = data;
  pc.listItems = ["true", "false", "na"]
  pc.ok = function () {
    //{...}
    //alert("You clicked the ok button."); 
    let body = {
      "immunizations": pc.data.immunizations,
      "offerReceived": pc.data.offerReceived,
      "cgpa": pc.data.cgpa,
      "criminalCheck": pc.data.criminalCheck,
      "acceptanceForm": pc.data.acceptanceForm,
      "childAbuse": pc.data.childAbuse,
      "bannerId": pc.data.bannerId,
      "CPR": pc.data.CPR
    }
    studentService.updateStudent(body).then(function (response) {
      console.log(response)
      $rootScope.getStudents($rootScope.currentPage2)
      // $scope.students = response.data.data
      //console.log($scope.students[0])

    }, function (error) {
      // $scope.status = 'Unable to insert customer: ' + error.message;
    });
    $uibModalInstance.close("save");
    //$rootScope.getStudents($rootScope.currentPage2)

  };

  pc.cancel = function () {
    //{...}
   // alert("You clicked the cancel button.");
    $uibModalInstance.dismiss('cancel');
  };
});

app.controller('ModalConfirmCtrl', function ($uibModalInstance, studentService, data, $rootScope) {
  var pc = this;
  pc.data = data;

  pc.ok = function () {

    $uibModalInstance.close("save");

  };

  pc.cancel = function () {
    //{...}
    //alert("You clicked the cancel button.");
    $uibModalInstance.dismiss('cancel');
  };
});