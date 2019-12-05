var turmasController = function($scope, $mdToast, TurmaApi) {

  $scope.turmas = [];

  let listar = function() {
      TurmaApi.listar(nome)
        .then(function(response) {
          $scope.turmas = response.data;
        })
        .catch(function(error) {

        });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      TurmaApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.turmas = response.data;
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

app.controller('TurmasController', turmasController);
