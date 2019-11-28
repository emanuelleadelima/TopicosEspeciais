// Inicializar o módulo.
let nomeApp = 'EscolaWebApp';
let modulos = ['ngMaterial', 'ngMessages', 'ngRoute', 'ngAnimate', 'ngAria'];

var app = angular.module(nomeApp, modulos);

var formatar = function(mascara, documento){
  var i = documento.value.length;
  var saida = mascara.substring(0,1);
  var texto = mascara.substring(i);

  if (texto.substring(0,1) != saida){
    documento.value += texto.substring(0,1);
  }
}
