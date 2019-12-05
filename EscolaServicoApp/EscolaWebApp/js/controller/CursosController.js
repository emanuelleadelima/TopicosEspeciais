var cursosController = function($scope, $mdToast, CursoApi) {

  $scope.cursos = [];

  let listar = function() {
      CursoApi.listar(nome)
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
    $scope.apresentacoes = [];
  };

}

app.controller('CursosController', cursosController);
