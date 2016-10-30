(function(){

    var app = angular.module('longevity_diet', ['ngResource']);

    app.config(['$resourceProvider', function($resourceProvider) {
        // Don't strip trailing slashes from calculated URLs
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }]);
    
    app.factory("Food", function($resource) {
        return $resource("/longevity/api/food/:id");
    });

    app.controller('MainController', ['$http', 'Food', function($http, Food) {

        var t = this;

        Food.get({ id: 1 }, function(data) {
            t.foo = data;
        });
        
    }]);

})();
