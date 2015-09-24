(function(){
    var app = angular.module("showProgress.services", []);
    app.factory("mainServices", ["$http", function($http){
        return {
            loadAvailableHosts: function($scope){
                $http.get('/usetracker/get_available_hosts/').
                    success(function(data, status, headers, config) {
                        $scope.availableHosts = data.hosts;
                    }).
                    error(function(data, status, headers, config) {
                        $scope.availableHosts = [];
                    });
            },
            loadAvailableProtocols: function($scope){
                $http.get('/usetracker/get_available_protocols/').
                    success(function(data, status, headers, config) {
                        $scope.availableProtocols = data.protocols;
                    }).
                    error(function(data, status, headers, config) {
                        $scope.availableProtocols = [];
                    });
            },
            loadAvailableUsers: function($scope){
                $http.get('/usetracker/get_available_users/').
                    success(function(data, status, headers, config) {
                        $scope.availableUsers = data.users;
                    }).
                    error(function(data, status, headers, config) {
                        $scope.availableUsers = [];
                    });
            },
            loadAvailableFields: function($scope){
                $http.get('/usetracker/get_available_fields/').
                    success(function(data, status, headers, config) {
                        $scope.availableFields = data.fields;
                    }).
                    error(function(data, status, headers, config) {
                        $scope.availableFields = [];
                    });
            },
            loadFilteredData: function($scope){
                params = {}
                for(key in $scope.progressChartFilters){
                    params[key] = $scope.progressChartFilters[key];
                }
                $http.get('/usetracker/get_filtered_data/', {'params': params}).
                    success(function(data, status, headers, config) {
                        $scope.rawData = data.rawdata;
                        $scope.progressChartData = data.data;
                        $scope.progressChartLabels = data.labels;
                        $scope.progressChartSeries = data.series;
                    }).
                    error(function(data, status, headers, config) {
                        $scope.progressChartData = [];
                        $scope.progressChartLabels = [];
                        $scope.progressChartSeries = [];
                    });
            },
        }
    }]);
})()
