var professoresController = function($scope, $mdToast, ProfessorApi) {

  $scope.professores = [];

  $scope.listar = function() {
    console.log("Listando")
    ProfessorApi.listar()
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
    $scope.professores = [];
  };

}

app.controller('ProfessoresController', professoresController);
