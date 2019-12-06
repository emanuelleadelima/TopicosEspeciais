var cursosController = function($scope, $mdToast, CursoApi) {

  $scope.cursos = [];

  $scope.listar = function() {
    console.log("Listando")
    CursoApi.listar()
      .then(function(response) {
        $scope.cursos = response.data;
      })
      .catch(function(error) {

      });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      CursoApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.cursos = response.data;
        })
        .catch(function(error) {

        });
    }
  };

  $scope.limparBusca = function() {
    $scope.nome = "";
    $scope.cursos = [];
  };

}

app.controller('CursosController', cursosController);
