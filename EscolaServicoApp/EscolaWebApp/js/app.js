// Inicializar o módulo.
let nomeApp = 'EscolaWebApp';
let modulos = [];

var app = angular.module(nomeApp, modulos);

//Estrutura básica para uma função no controlador.
//toda variável associada ao $scope: se eu modificar no JS, modifico na tela.
var MeuPrimeiroController = function($scope){
  $scope.logradouro = 'Outro valor';
  $scope.numero1 = 0;
  $scope.numero2 = 0;

  $scope.somar = function(numero1, numero2){
    $scope.resultado = numero1 + numero2;
  }
}

app.controller('MeuPrimeiroController', MeuPrimeiroController);

var MeuSegundoController = function($scope){
  $scope.logradouro = 'Outro valor';
}

app.controller('MeuSegundoController', MeuSegundoController);
