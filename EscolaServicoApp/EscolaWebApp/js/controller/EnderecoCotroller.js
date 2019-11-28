//Endereco.html
var enderecoController = function($scope, $mdToast, enderecoApi){
  $scope.endereco = {};
  let endereco = $scope.endereco;

  $scope.cadastrar = function(){
    enderecoApi.cadastrar(endereco)
    .then(function(response) {
      console.log("Requisição enviada e recebida com sucesso!");
      console.log(response);
    })
    .catch(function(error) {
      var toast = $mdToast.simple()
        .textContent('Algum problema ocorreu no envio dos dados :c tururuuu...')
        .position('top right')
        .action('OK')
        .hideDelay(6000);
      $mdToast.show(toast);
    });
  }
}

app.controller('EnderecoController', enderecoController);
