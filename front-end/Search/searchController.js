app.controller("searchCtrl", ['$scope', 'jobService', function ($scope, jobService) {
  $scope.path = "file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/front-end/Navbar/home.html#!/"
  $scope.city = "";
  $scope.province = "";
  $scope.category = "";
  $scope.type = "";
  $scope.searchValue = ''

  $scope.totalItems = 0;
  $scope.currentPage = 1;
  $scope.maxSize = 5;
  $scope.itemsPerPage = 1;


  $scope.getDrops =function () {
    jobService.getDrops().then(function (response) {
      console.log(response.data)
      data = response.data
      $scope.cities = data.cities
      $scope.provinces = data.provinces
      $scope.types = data.types
      $scope.categories = data.categories

    })
  }

  $scope.getDrops()
  $scope.pageChanged = function () {

    $scope.getJobs($scope.currentPage)


  };
  $scope.getJobs = function (page) {
    jobService.searchJobs($scope.city, $scope.province, $scope.type, $scope.category, $scope.searchValue, page).then(function (response) {
      console.log(response)
      $scope.jobs = response.data.data
      if ($scope.jobs[0])
        $scope.totalItems = $scope.jobs[0].count;
      else
        $scope.totalItems = 0
      console.log($scope.jobs[0])

    }, function (error) {
      // $scope.status = 'Unable to insert customer: ' + error.message;
    });
  }

  $scope.getJobs(1);
  $scope.agency = function (job) {
    console.log(window.location.href + "register")
    window.localStorage.setItem('job',JSON.stringify(job))
    window.location.href = $scope.path + "student/agency";
  };
}]);