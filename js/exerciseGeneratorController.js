app.controller("ExerciseGeneratorCtrl", ["$scope", "exerciseService", "setsRepsService", 
	function($scope, exerciseService, setsRepsService) {
		$scope.exerciseChoices = ["legs", "glutes", "calves", "chest", "back", "triceps", "biceps", "shoulders"];
		$scope.exercises;
		$scope.notUnique = null;

		$scope.loadExerciseData = function(muscleGroup, exerciseAmount){
			console.log("getting exercises...");
			exerciseService.getExercises().then(function(response){
				$scope.responseData = response;
				if(muscleGroup){
					var stringifiedResponse = JSON.stringify(response);
					$scope.responseData = $scope.lookUpKeyVal(JSON.parse(stringifiedResponse), {bodyPart : muscleGroup});
				}
			    
			    $scope.applyResponseData($scope.responseData, exerciseAmount);
			});
		};

		$scope.lookUpKeyVal = function(obj, keyValPair) {
			return obj.filter(function(object){
				return Object.keys(keyValPair).every(function(key){
					return object[key] == keyValPair[key];
				})
			})
		};

		$scope.applyResponseData = function(newExercises, exerciseAmount){
			$scope.exercises = newExercises;
			$scope.parseDataFromArray($scope.exercises, exerciseAmount);
		};

		$scope.parseDataFromArray = function(arr, exerciseAmount){
			for(var i = 0; i < arr.length; i++){
				var data = arr[i];
				if(data.hasOwnProperty("exercise")) {
					var exercise = data["exercise"];
					console.log("exercise: ", data["exercise"]);
					if(data.hasOwnProperty("variations")){
						var variations = data["variations"];
						$scope.parseVariations(variations, exerciseAmount);
					}
				}
			}
		};

		$scope.parseVariations = function(obj, exerciseAmount){
			var a = [];
			for(key in obj){
				var variation = obj[key];
				a.push($scope.getRandomWorkout(variation, exerciseAmount));
			}	

			var b = [];
			// for(var i = 0; i < a.length; i++){
			// 	console.log("i", a[i]);
			// 	for(var j = 0; j < a[i].length; j++){
			// 		console.log("j", a[i][j]);
			// 	}
			// }
		}

		// $scope.getUniqueRandomWorkout = function(arr, num){
		// 	var a = [];
			
		// 	for(var i = 0; i < num; i++){
		// 		var random = Math.floor(Math.random() * arr.length);
		// 		function getUnique(){
		// 			if(a has this index){
		// 				getUnique();
		// 			}
		// 			else {
		// 				a.push(arr[random]);				
		// 			}
		// 		}
		// 	}		
		// 	console.log("a", a);
		// };

		$scope.getRandomWorkout = function(arr, num){
			$scope.notUnique = "We apologize but we do not have enough exercises archived to produce that many unique workouts.";

			var a = [];
			for(var i = 0; i < num; i++){
				var random = Math.floor(Math.random() * arr.length);
				a.push(arr[random]);
			}

			return a;
		};

// check to see if number selected exceeds the amount of user exercises, if it does then

}]);



