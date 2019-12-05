var professoresController = function($scope, $mdToast, ProfessorApi) {

  $scope.professores = [];

  let listar = function() {
      ProfessorApi.listar(nome)
        .then(function(response) {
          $scope.professores = response.data;
        })
        .catch(function(error) {

        });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      ProfessorApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.professores = response.data;
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

app.controller('ProfessoresController', professoresController);
