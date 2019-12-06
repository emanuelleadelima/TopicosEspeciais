var turnosController = function($scope, $mdToast, TurnoApi) {

  $scope.turnos = [];

  $scope.listar = function() {
    console.log("Listando")
    TurnoApi.listar()
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
    $scope.turnos = [];
  };

}

app.controller('TurnosController', turnosController);
