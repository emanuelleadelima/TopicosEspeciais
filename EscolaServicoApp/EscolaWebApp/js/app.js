// Inicializar o módulo.
let nomeApp = 'EscolaWebApp';
let modulos = ["ngMessages"];

var app = angular.module(nomeApp, modulos);

//Estrutura básica para uma função no controlador.
//toda variável associada ao $scope: se eu modificar no JS, modifico na tela.

//index.html
var homeController = function($scope){
  $scope.nome = "";

  $scope.desejarBoasVindas = function() {
    let nome = $scope.nome;
    $scope.mensagem = "Olá, " + nome;
  }
}

app.controller('HomeController', homeController);

//Endereco.html
var enderecoController = function($scope){
  $scope.logradouro = "";
  $scope.complemento = "";
  $scope.bairro = "";
  $scope.cep = "";
  $scope.numero = "";

  $scope.nome2 = "MiniTeste";

  $scope.teste = function(){
    let nome2 = $scope.nome2;
    $scope.mensagem2 = "Isto é um " + nome2;
    $scope.FormAJS.$setPristine();
    $scope.FormAJS.$setUntouched();
  }
}

app.controller('EnderecoController', enderecoController);

//Escola.html
var escolaController = function($scope){
  $scope.nome = "";
  $scope.id_endereco = "";
  $scope.id_campus = "";

  $scope.nome2 = "MiniTeste";

  $scope.teste = function(){
    let nome2 = $scope.nome2;
    $scope.mensagem2 = "Isto é um " + nome2;
    $scope.FormAJS.$setPristine();
    $scope.FormAJS.$setUntouched();
  }
}

app.controller('EscolaController', escolaController);

//Aluno.html
var alunoController = function($scope){
  $scope.nome = "";
  $scope.matricula = "";
  $scope.cpf = "";
  $scope.nascimento = "";
  $scope.id_endereco = "";
  $scope.id_curso = "";

  $scope.nome2 = "MiniTeste";

  $scope.teste = function(){
    let nome2 = $scope.nome2;
    $scope.mensagem2 = "Isto é um " + nome2;
    $scope.FormAJS.$setPristine();
    $scope.FormAJS.$setUntouched();
  }
}

app.controller('AlunoController', alunoController);

//Professor.html
var professorController = function($scope){
  $scope.nome = "";
  $scope.id_endereco = "";

  $scope.nome2 = "MiniTeste";

  $scope.teste = function(){
    let nome2 = $scope.nome2;
    $scope.mensagem2 = "Isto é um " + nome2;
    $scope.FormAJS.$setPristine();
    $scope.FormAJS.$setUntouched();
  }
}

app.controller('ProfessorController', professorController);

//Disciplina.html
var disciplinaController = function($scope){
  $scope.nome = "";
  $scope.id_professor = "";

  $scope.nome2 = "MiniTeste";

  $scope.teste = function(){
    let nome2 = $scope.nome2;
    $scope.mensagem2 = "Isto é um " + nome2;
    $scope.FormAJS.$setPristine();
    $scope.FormAJS.$setUntouched();
  }
}

app.controller('DisciplinaController', disciplinaController);

//Curso.html
var cursoController = function($scope){
  $scope.nome = "";
  $scope.id_turno = "";

  $scope.nome2 = "MiniTeste";

  $scope.teste = function(){
    let nome2 = $scope.nome2;
    $scope.mensagem2 = "Isto é um " + nome2;
    $scope.FormAJS.$setPristine();
    $scope.FormAJS.$setUntouched();
  }
}

app.controller('CursoController', cursoController);

//Campus.html
var campusController = function($scope){
  $scope.sigla = "";
  $scope.cidade = "";

  $scope.nome2 = "MiniTeste";

  $scope.teste = function(){
    let nome2 = $scope.nome2;
    $scope.mensagem2 = "Isto é um " + nome2;
    $scope.FormAJS.$setPristine();
    $scope.FormAJS.$setUntouched();
  }
}

app.controller('CampusController', campusController);

//Turma.html
var turmaController = function($scope){
  $scope.nome = "";
  $scope.id_curso = "";

  $scope.nome2 = "MiniTeste";

  $scope.teste = function(){
    let nome2 = $scope.nome2;
    $scope.mensagem2 = "Isto é um " + nome2;
    $scope.FormAJS.$setPristine();
    $scope.FormAJS.$setUntouched();
  }
}

app.controller('TurmaController', turmaController);

//Turno.html
var turnoController = function($scope){
  $scope.nome = "";

  $scope.nome2 = "MiniTeste";

  $scope.teste = function(){
    let nome2 = $scope.nome2;
    $scope.mensagem2 = "Isto é um " + nome2;
    $scope.FormAJS.$setPristine();
    $scope.FormAJS.$setUntouched();
  }
}

app.controller('TurnoController', turnoController);
