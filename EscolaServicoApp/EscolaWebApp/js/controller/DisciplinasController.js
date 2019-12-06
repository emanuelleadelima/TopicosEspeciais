var disciplinasController = function($scope, $mdToast, DisciplinaApi) {

  $scope.disciplinas = [];

  $scope.listar = function() {
    console.log("Listando")
    DisciplinaApi.listar()
      .then(function(response) {
        $scope.disciplinas = response.data;
      })
      .catch(function(error) {

      });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      DisciplinaApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.disciplinas = response.data;
        })
        .catch(function(error) {

        });
    }
  };

  $scope.limparBusca = function() {
    $scope.nome = "";
    $scope.disciplinas = [];
  };

}

app.controller('DisciplinasController', disciplinasController);
