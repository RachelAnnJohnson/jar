directivesModule.directive('checkbox', [function(){

		template: checkboxTemplateDirective.html,
		scope: {
			'name': '@',
			'ngRepeat': '=',
			'ngChecked': '='
		},
		replace: true

}]);