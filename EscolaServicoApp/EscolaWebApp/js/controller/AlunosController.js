var alunosController = function($scope, $mdToast, AlunoApi) {

  $scope.alunos = [];

  let listar = function() {
      AlunoApi.listar(nome)
        .then(function(response) {
          $scope.alunos = response.data;
        })
        .catch(function(error) {

        });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      AlunoApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.alunos = response.data;
        })
        .catch(function(error) {

        });
    }
  };

  $scope.limparBusca = function() {
    $scope.nome = "";
    $scope.apresentacoes = [];
  };

}

app.controller('AlunosController', alunosController);
