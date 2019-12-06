var escolasController = function($scope, $mdToast, EscolaApi) {

  $scope.escolas = [];

  $scope.listar = function() {
    console.log("Listando")
    EscolaApi.listar()
      .then(function(response) {
        $scope.escolas = response.data;
      })
      .catch(function(error) {

      });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      EscolaApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.escolas = response.data;
        })
        .catch(function(error) {

        });
    }
  };

  $scope.limparBusca = function() {
    $scope.nome = "";
    $scope.escolas = [];
  };

}

app.controller('EscolasController', escolasController);
