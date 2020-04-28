app.factory('studentService', ['$http', function($http) {

    var urlBase = 'http://127.0.0.1:5000';
    var studentService = {};

    studentService.getStudents = function (page) {
        return $http.get(urlBase+"/admin/"+page);
    };

    studentService.searchStudents = function (searchValue,searchType,page) {
        return $http.get(urlBase+"/admin/search?searchValue="+searchValue+"&searchType="+searchType+"&page="+page);
    };

    studentService.getStudent = function (id) {
        return $http.get(urlBase + '/' + id);
    };

    studentService.insertStudent = function (cust) {
        return $http.post(urlBase+'/admin/updateSupp/', cust);
    };

    studentService.activateStudent = function (cust) {
        return $http.post(urlBase+'/admin/activateStud', cust);
    };

    studentService.updateStudent = function (cust) {
        return $http.post(urlBase+'/admin/updateSupp', cust);
    };

    studentService.deleteStudent = function (id) {
        return $http.delete(urlBase + '/' + id);
    };

    studentService.getOrders = function (id) {
        return $http.get(urlBase + '/' + id + '/orders');
    };

    studentService.logout = function () {
        return $http.post(urlBase + '/auth/logout' );
    };
    
    
      
    return studentService;
}]);

