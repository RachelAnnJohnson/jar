app.service("setsRepsService", ["$http", function($http) {
	return({
		getSetsReps : getSetsReps
	});

	function getSetsReps() {
		var request = $http({
			method: "get",
			url: "js/setsReps.json",
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
		return 'error';
	}
}]);