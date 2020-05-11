app.factory('jobService', ['$http', function($http) {

    var urlBase = 'http://127.0.0.1:5000';
    var jobService = {};

    jobService.getDrops = function () {
        return $http.get(urlBase+"/agency/drops");
    };

    jobService.searchJobs = function (city,province,type,category,searchValue,page) {
        return $http.get(urlBase+"/agency/search?searchValue="+searchValue+"&city="+city+"&province="+province+"&type="+type+"&category="+category+"&page="+page);
    };

       
    
      
    return jobService;
}]);

