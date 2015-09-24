(function(){
    var app = angular.module("showProgress", ["chart.js", "showProgress.controllers", "showProgress.services", "showProgress.filters"]);
    app.config(function ($httpProvider) {
        $httpProvider.defaults.headers.put['Content-Type'] = 'application/x-www-form-urlencoded';
        $httpProvider.defaults.headers.post['Content-Type'] =  'application/x-www-form-urlencoded';
    });
})()
