var enderecosController = function($scope, $mdToast, EnderecosApi) {

  $scope.enderecos = [];

  $scope.listar = function() {
    console.log("Listando")
    EnderecosApi.listar()
      .then(function(response) {
        $scope.enderecos = response.data;
      })
      .catch(function(error) {

      });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      EnderecoApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.enderecos = response.data;
        })
        .catch(function(error) {

        });
    }
  };

  $scope.limparBusca = function() {
    $scope.nome = "";
    $scope.enderecos = [];
  };

}

app.controller('EnderecosController', enderecosController);
