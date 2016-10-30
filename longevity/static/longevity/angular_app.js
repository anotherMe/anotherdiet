(function(){

    var foo = {
        name: "Foo\'n\'tastic",
        canSpin: true,
        canRoll: false
    };

    var app = angular.module('longevity_diet', []);

    app.controller('FooController', function() {
        
        this.foo = foo;
        
    });

})();
