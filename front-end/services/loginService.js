app.factory('loginService', ['$http', function($http) {

    var urlBase = 'http://127.0.0.1:5000';
    var loginService = {};

   
    loginService.insertStudent = function (cust) {
        return $http.post(urlBase+'/user', cust);
    };

    loginService.login = function (student) {
        return $http.post(urlBase+'/auth/login', student)
    };
   
    loginService.logout = function () {
        return $http.post(urlBase + '/auth/logout' );
    };
    
    
      
    return loginService;
}]);

