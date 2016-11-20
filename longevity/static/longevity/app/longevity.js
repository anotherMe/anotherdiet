(function(){

    var app = angular.module('longevity_diet', ['ngResource']);

//    app.config(function($routeProvider) {
//        $routeProvider
//        .when("/", {
//            templateUrl : "main.htm"
//        })
//        .when("/red", {
//            templateUrl : "red.htm"
//        })
//        .when("/green", {
//            templateUrl : "green.htm"
//        })
//        .when("/blue", {
//            templateUrl : "blue.htm"
//        });
//    });

    app.config(['$resourceProvider', function($resourceProvider) {

        // Don't strip trailing slashes from calculated URLs
        $resourceProvider.defaults.stripTrailingSlashes = false;

    }]);

    app.factory("Food", function($resource) {
        return $resource("/longevity/api/food/:id");
    });

    app.controller('MainController', ['$scope', '$http', 'Food', function($scope, $http, Food) {

        console.log('HERE');
        console.log($scope);

        Food.get({ id: 1 }, function(data) {
            $scope.foo = data;
        });

        Food.get(function(payload) {
            $scope.foodList = payload.objects;
        });

        $scope.search = function () {

            var successCallback = function (payload) {
                $scope.foodList = payload.data.objects;
            };

            var errorCallback = function () { console.log('There was an error retrieving food list'); };

            $http({
                url: '/longevity/api/food/',
                method: 'GET',
                params: {'nome__contains': $scope.searchString}
            }).then(successCallback, errorCallback);

        }
        
    }]);

})();
