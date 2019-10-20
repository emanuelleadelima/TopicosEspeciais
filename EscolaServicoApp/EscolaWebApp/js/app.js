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

//Aluno.html
var alunoController = function($scope){
  $scope.aluno = {};

  $scope.cadastrar = function(){
    delete $scope.aluno;
    $scope.alunoform.$setPristine();
  }
}

app.controller('AlunoController', alunoController);

//Campus.html
var campusController = function($scope){
  $scope.campus = {};

  $scope.cadastrar = function(){
    delete $scope.campus;
    $scope.campusform.$setPristine();
  }
}

app.controller('CampusController', campusController);

//Curso.html
var cursoController = function($scope){
  $scope.curso = {};

  $scope.cadastrar = function(){
    delete $scope.curso;
    $scope.cursoform.$setPristine();
  }
}

app.controller('CursoController', cursoController);

//Disciplina.html
var disciplinaController = function($scope){
  $scope.disciplina = {};

  $scope.cadastrar = function(){
    delete $scope.disciplina;
    $scope.disciplinaform.$setPristine();
  }
}

app.controller('DisciplinaController', disciplinaController);

//Endereco.html
var enderecoController = function($scope){
  $scope.endereco = {};

  $scope.cadastrar = function(){
    delete $scope.endereco;
    $scope.enderecoform.$setPristine();
  }
}

app.controller('EnderecoController', enderecoController);

//Escola.html
var escolaController = function($scope){
  $scope.escola = {};

  $scope.cadastrar = function(){
    delete $scope.escola;
    $scope.escolaform.$setPristine();
  }
}

app.controller('EscolaController', escolaController);

//Professor.html
var professorController = function($scope){
  $scope.professor = {};

  $scope.cadastrar = function(){
    delete $scope.professor;
    $scope.professorform.$setPristine();
  }
}

app.controller('ProfessorController', professorController);

//Turma.html
var turmaController = function($scope){
  $scope.turma = {};

  $scope.cadastrar = function(){
    delete $scope.turma;
    $scope.turmaform.$setPristine();
  }
}

app.controller('TurmaController', turmaController);

//Turno.html
var turnoController = function($scope){
  $scope.turno = {};

  $scope.cadastrar = function(){
    delete $scope.turno;
    $scope.turnoform.$setPristine();
  }
}

app.controller('TurnoController', turnoController);
