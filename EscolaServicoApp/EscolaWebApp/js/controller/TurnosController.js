var turnosController = function($scope, $mdToast, TurnoApi) {

  $scope.turnos = [];

  let listar = function() {
      TurnoApi.listar(nome)
        .then(function(response) {
          $scope.turnos = response.data;
        })
        .catch(function(error) {

        });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      TurnoApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.turnos = response.data;
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

app.controller('TurnosController', turnosController);
