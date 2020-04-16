app.factory('studentService', ['$http', function($http) {

    var urlBase = 'http://127.0.0.1:5000';
    var studentService = {};

    studentService.getStudents = function () {
        return $http.get(urlBase);
    };

    studentService.getStudent = function (id) {
        return $http.get(urlBase + '/' + id);
    };

    studentService.insertStudent = function (cust) {
        return $http.post(urlBase, cust);
    };

    studentService.updateStudent = function (cust) {
        return $http.put(urlBase + '/' + cust.ID, cust)
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

