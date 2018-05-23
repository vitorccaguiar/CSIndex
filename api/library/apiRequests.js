function getNumberOfPublicationsByConferences(area, conference, resultPanel) {
  $.ajax({
    type: "GET",
    url: "http://localhost:8080/publications/areas/conferences?area=" + area + "&conference=" + conference,
	success: function(data) {
		$("#" + resultPanel).val(data);
	}
  });
}

function getScoresByDepartments(area, department, resultPanel) {
  $.ajax({
    type: "GET",
    url: "http://localhost:8080/scores/areas/departments?area=" + area + "&department=" + department,
    success: function (data) {
      $("#" + resultPanel).val(data);
    }
  });
}

function getNumberOfProfessorsByDepartments(area, department, resultPanel) {
  $.ajax({
    type: "GET",
    url: "http://localhost:8080/professors/areas/departments?area=" + area + "&department=" + department,
    success: function (data) {
      $("#" + resultPanel).val(data);
    }
  });
}

function getPapers(area, year, department, professor, resultPanel) {
	if (year == '' && department == '' && professor == '') {
   $.ajax({
     type: "GET",
     url: "http://localhost:8080/papers/areas?area=" + area,
     success: function (data) {
       $("#" + resultPanel).val(data);
     }
   });
	}
	if (year != '' && department == '' && professor == '') {
   $.ajax({
     type: "GET",
     url: "http://localhost:8080/papers/areas?area=" + area + "&year=" + year,
     success: function (data) {
       $("#" + resultPanel).val(data);
     }
   });
	}
	if (year == '' && department != '' && professor == '') {
   $.ajax({
     type: "GET",
     url: "http://localhost:8080/papers/areas?area=" + area + "&department=" + department,
     success: function (data) {
       $("#" + resultPanel).val(data);
     }
   });
	}
	if (year == '' && department == '' && professor != '') {
   $.ajax({
     type: "GET",
     url: "http://localhost:8080/papers/areas?area=" + area + "&professor=" + professor,
     success: function (data) {
       $("#" + resultPanel).val(data);
     }
   });
	}
}