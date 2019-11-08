// Inicializar o módulo.
let nomeApp = 'EscolaWebApp';
let modulos = ['ngMaterial', 'ngMessages'];

var app = angular.module(nomeApp, modulos);

//toda variável associada ao $scope: se eu modificar no JS, modifico na tela.

var formatar = function(mascara, documento){
  var i = documento.value.length;
  var saida = mascara.substring(0,1);
  var texto = mascara.substring(i);

  if (texto.substring(0,1) != saida){
    documento.value += texto.substring(0,1);
  }
}

//Aluno.html
var alunoController = function($scope, $mdToast, alunoApi){
  $scope.aluno = {};
  let aluno = $scope.aluno;

  $scope.cadastrar = function(){
    alunoApi.cadastrar(aluno)
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

app.controller('AlunoController', alunoController);

// Aluno - Factory
var alunoFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/alunos")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/alunos/" + encodeURI(id))
  };

  var _cadastrar = function(aluno) {
    return $http.post(baseUrl + "/aluno", aluno)
  };

  var _atualizar = function(aluno) {
    return $http.put(baseUrl+ "/aluno/" + encodeURI(id), aluno)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("alunoApi", alunoFactory);

//Campus.html
var campusController = function($scope, $mdToast, campusApi){
  $scope.campus = {};
  let campus = $scope.campus;

  $scope.cadastrar = function(){
    campusApi.cadastrar(campus)
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

app.controller('CampusController', campusController);

// Campus - Factory
var campusFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/campi")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/campi/" + encodeURI(id))
  };

  var _cadastrar = function(campus) {
    return $http.post(baseUrl + "/campus", campus)
  };

  var _atualizar = function(campus) {
    return $http.put(baseUrl+ "/campus/" + encodeURI(id), campus)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("campusApi", campusFactory);

//Curso.html
var cursoController = function($scope, $mdToast, cursoApi){
  $scope.curso = {};
  let curso = $scope.curso;

  $scope.cadastrar = function(){
    cursoApi.cadastrar(curso)
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

app.controller('CursoController', cursoController);

// Curso - Factory
var cursoFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/cursos")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/cursos/" + encodeURI(id))
  };

  var _cadastrar = function(curso) {
    return $http.post(baseUrl + "/curso", curso)
  };

  var _atualizar = function(curso) {
    return $http.put(baseUrl+ "/curso/" + encodeURI(id), curso)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("cursoApi", cursoFactory);

//Disciplina.html
var disciplinaController = function($scope, $mdToast, disciplinaApi){
  $scope.disciplina = {};
  let disciplina = $scope.disciplina;

  $scope.cadastrar = function(){
    disciplinaApi.cadastrar(disciplina)
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

app.controller('DisciplinaController', disciplinaController);

// Disciplina - Factory
var disciplinaFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/disciplinas")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/disciplinas/" + encodeURI(id))
  };

  var _cadastrar = function(disciplina) {
    return $http.post(baseUrl + "/disciplina", disciplina)
  };

  var _atualizar = function(disciplina) {
    return $http.put(baseUrl+ "/disciplina/" + encodeURI(id), disciplina)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("disciplinaApi", disciplinaFactory);

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

// Endereco - Factory
var enderecoFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/enderecos")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/enderecos/" + encodeURI(id))
  };

  var _cadastrar = function(endereco) {
    return $http.post(baseUrl + "/endereco", endereco)
  };

  var _atualizar = function(curso) {
    return $http.put(baseUrl+ "/endereco/" + encodeURI(id), endereco)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("enderecoApi", enderecoFactory);

//Escola.html
var escolaController = function($scope, $mdToast, escolaApi){
  $scope.escola = {};
  let escola = $scope.escola;

  $scope.cadastrar = function(){
    escolaApi.cadastrar(escola)
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

app.controller('EscolaController', escolaController);

// Escola - Factory
var escolaFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/escolas")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/escolas/" + encodeURI(id))
  };

  var _cadastrar = function(escola) {
    return $http.post(baseUrl + "/escola", escola)
  };

  var _atualizar = function(escola) {
    return $http.put(baseUrl+ "/escola/" + encodeURI(id), escola)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("escolaApi", escolaFactory);

//Professor.html
var professorController = function($scope, $mdToast, professorApi){
  $scope.professor = {};
  let professor = $scope.professor;

  $scope.cadastrar = function(){
    professorApi.cadastrar(professor)
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

app.controller('ProfessorController', professorController);

// Professor - Factory
var professorFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/professores")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/professores/" + encodeURI(id))
  };

  var _cadastrar = function(professor) {
    return $http.post(baseUrl + "/professor", professor)
  };

  var _atualizar = function(professor) {
    return $http.put(baseUrl+ "/professor/" + encodeURI(id), professor)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("professorApi", professorFactory);

//Turma.html
var turmaController = function($scope, $mdToast, turmaApi){
  $scope.turma = {};
  let turma = $scope.turma;

  $scope.cadastrar = function(){
    turmaApi.cadastrar(turma)
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

app.controller('TurmaController', turmaController);

// Turma - Factory
var turmaFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/turmas")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/turmas/" + encodeURI(id))
  };

  var _cadastrar = function(turma) {
    return $http.post(baseUrl + "/turma", turma)
  };

  var _atualizar = function(turma) {
    return $http.put(baseUrl+ "/turma/" + encodeURI(id), turma)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("turmaApi", turmaFactory);

//Turno.html
var turnoController = function($scope, $mdToast, turnoApi){
  $scope.turno = {};
  let turno = $scope.turno;

  $scope.cadastrar = function(){
    turnoApi.cadastrar(turno)
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

app.controller('TurnoController', turnoController);

// Turno - Factory
var turnoFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/turnos")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/turnos/" + encodeURI(id))
  };

  var _cadastrar = function(turno) {
    return $http.post(baseUrl + "/turno", turno)
  };

  var _atualizar = function(turno) {
    return $http.put(baseUrl+ "/turno/" + encodeURI(id), turno)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("turnoApi", turnoFactory);
