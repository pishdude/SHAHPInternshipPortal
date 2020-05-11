app.controller("agencyCtrl", function($scope) {
  $scope.path="file:///D:/Work/InternshipPortal/SHAHPInternshipPortal/front-end/Navbar/home.html#!/"
  $scope.agency = "New Hampshire Hospital";
  $scope.description ="A research facility with a primary focus directed at providing the most effective, modern,"
   +"and compassionate treatment to individuals with psychiatric illness. The in-patient clinical services offered at the facility support individuals diagnosed with eating disorders, mood disorders, schizophrenia, children and adolescent mental health, and community-based outreach."
  $scope.location="Halifax,NS";
  $scope.website="www.example.com";
  $scope.categories="Children,Aged"
 

  $scope.load = function(){
    $scope.job = JSON.parse(window.localStorage.getItem('job'));
    console.log($scope.job.name)
    $scope.agency = $scope.job.name
    $scope.description = $scope.job.description
    $scope.location = $scope.job.locations[0].City +","+ $scope.job.locations[0].Province
    $scope.website= $scope.job.applicationprocedure.website
    $scope.categories =""
    for (let index = 0; index < $scope.job.categories.length; index++) {
      $scope.categories = $scope.categories + $scope.job.categories[index].category+";"
      
    }
    $scope.supervisorName = $scope.job.supervisor.name
    $scope.supervisorEmail = $scope.job.supervisor.email
    
  }

  $scope.load()
  });