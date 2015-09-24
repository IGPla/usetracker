(function(){
    var app = angular.module("showProgress.controllers", []);
    app.controller("mainController", ["$scope", "mainServices", function($scope, mainServices){
        $scope.rawData = [];
        $scope.progressChartData = [];
        $scope.progressChartSeries = [];
        $scope.progressChartLabels = [];
        $scope.availableProtocols = [];
        $scope.availableHosts = [];
        $scope.availableUsers = [];
        $scope.availableGroups = ["minute", "hour", "day", "month"]
        $scope.availableChartTypes = ["Requests started at", "Requests end at", "Execution time"]
        $scope.availableFields = [];
        $scope.progressChartFilters = {
            fromdate: "",
            todate: "",
            protocol: "",
            host: "",
            path: "",
            getparams: "",
            headers: "",
            postpayload: "",
            user: "",
            exceptiontext: "",
            minexecutiontime: 0,
            maxexecutiontime: 10,
            groupby: $scope.availableGroups[0],
            charttype: $scope.availableChartTypes[0]
        }
        mainServices.loadAvailableHosts($scope);
        mainServices.loadAvailableProtocols($scope);
        mainServices.loadAvailableFields($scope);
        mainServices.loadAvailableUsers($scope);

        $scope.$watch("progressChartFilters",
                      function(){
                          mainServices.loadFilteredData($scope);
                      },
                      1);

        $scope.tabSelector = "chart";
    }]);
})()
