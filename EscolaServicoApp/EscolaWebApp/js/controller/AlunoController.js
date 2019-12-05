//Aluno.html
var alunoController = function($scope, $mdToast, $state, alunoApi){

  $scope.aluno = {};

  $scope.cadastrar = function(){
    let aluno = $scope.aluno;

    var data= moment(aluno.nascimento, "DD/MM/YYYY");
    aluno.nascimento = data.format("YYYY-MM-DD");

    alunoApi.cadastrar(aluno)
      .then(function(response) {
        var toast = $mdToast.simple()
          .textContent('O aluno foi cadastrado com sucesso =D')
          .position('top right')
          .action('OK')
          .hideDelay(6000);
        $mdToast.show(toast);

        limparFormulario();
      })
      .catch(function(error) {
        var toast = $mdToast.simple()
          .textContent('Algum problema ocorreu no envio dos dados :c tururuuu...')
          .position('top right')
          .action('OK')
          .hideDelay(6000);
        $mdToast.show(toast);
      });
  };

  let limparFormulario = function () {

        // Reinicializa a variável aluno.
        angular.copy({}, $scope.aluno);

        // Reinicializa o estado do campo para os eventos e validação.
        // É necessário indicar o atributo name no formulário <form>
        $scope.alunoForm.$setPristine();
        $scope.alunoForm.$setUntouched();
        $scope.alunoForm.$setValidity();
  };
}

app.controller('AlunoController', alunoController);
