app.service("exerciseService", ["$http", "$q", function($http, $q) {
	return({
		getExercises : getExercises
	});

	function getExercises() {
		var request = $http({
			method: "get",
			url: "js/exercises.json",
			params: {
				action: "get"
			}
		});
		return request.then(success, error)
	};

	function success(response){
		return response.data;
	};

	function error(response){
        if (!response.data) {
           return $q.reject("An unknown error has occurred.");
        }
        return $q.reject(response.data);
	}
}]);