var enderecosController = function($scope, $mdToast, EnderecoApi) {

  $scope.enderecos = [];

  let listar = function() {
      EnderecoApi.listar(nome)
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
    $scope.apresentacoes = [];
  };

}

app.controller('EnderecosController', enderecosController);
