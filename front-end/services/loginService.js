app.factory('dataFactory', ['$http', function($http) {

    var urlBase = 'http://127.0.0.1:5000/';
    var dataFactory = {};

    dataFactory.getCustomers = function () {
        return $http.get(urlBase);
    };

    dataFactory.getCustomer = function (id) {
        return $http.get(urlBase + '/' + id);
    };

    dataFactory.insertCustomer = function (cust) {
        return $http.post(urlBase, cust);
    };

    dataFactory.updateCustomer = function (cust) {
        return $http.put(urlBase + '/' + cust.ID, cust)
    };

    dataFactory.deleteCustomer = function (id) {
        return $http.delete(urlBase + '/' + id);
    };

    dataFactory.getOrders = function (id) {
        return $http.get(urlBase + '/' + id + '/orders');
    };

    dataFactory.logout = function (cust) {
        return $http.post(urlBase + '/auth/logout', headers );
    };
    const headers = {headers:{
        'Content-Type': 'application/json',
        'Authorization': 'JWT ' + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1ODMzOTQwMjgsInN1YiI6MSwiZXhwIjoxNTgzNDgwNDMzfQ.CNPfaO6Q6DVHx_5LEoi8pyooCz1PIao5maVEXkAVUCA"
     } }; 
    
      
    return dataFactory;
}]);

