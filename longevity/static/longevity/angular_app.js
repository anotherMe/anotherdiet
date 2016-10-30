(function(){

    var app = angular.module('longevity_diet', ['ngResource']);

    app.config(['$resourceProvider', function($resourceProvider) {
        // Don't strip trailing slashes from calculated URLs
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }]);
    
    app.factory("Alimento", function($resource) {
        return $resource("/longevity/api/alimento/:id");
    });

    app.controller('MainController', ['$http', 'Alimento', function($http, Alimento) {

        var t = this;

        Alimento.get({ id: 1 }, function(data) {
            t.foo = data;
        });
        
    }]);

})();
