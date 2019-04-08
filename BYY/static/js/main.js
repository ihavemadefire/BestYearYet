//on load grab first value from each and display

$(document).load(function(){
  $('#getArea').on("click",function(e){
  let areaName = e.target.value;
  $("#getGoal").empty();
  $.ajax({
      url:'http://127.0.0.1:5000/areas/'+areaName}).done(function(area){
        $.each(area, function(key, value){
          $("#getGoal").append("<option value"+value+">"+value+"</option");
        });
      });
    });
});
$(document).ready(function(){
  $('#getGoal').on("click",function(e){
    let goalName = e.target.value;

  $.ajax({
    url:'http://127.0.0.1:5000/goals/'+goalName}).done(function(goal){
      $('#name').text(goal.name);
      $('#area').text(goal.area);
      $('#type').text(goal.type);
      $('#description').text(goal.description);
      $('#status').text(goal.status);
      $('#update_news').text(goal.update_news);
      $('#percent_complete').css("width", goal.percent_complete+"%");
      $('#percent_complete').text(goal.percent_complete)
    });
  });
});






$(document).ready(function(){
  $('#getArea').on("click",function(e){
  let areaName = e.target.value;
  $("#getGoal").empty();
  $.ajax({
      url:'http://127.0.0.1:5000/areas/'+areaName}).done(function(area){
        $.each(area, function(key, value){
          $("#getGoal").append("<option value"+value+">"+value+"</option");
        });
      });
    });
});
$(document).ready(function(){
  $('#getGoal').on("click",function(e){
    let goalName = e.target.value;

  $.ajax({
    url:'http://127.0.0.1:5000/goals/'+goalName}).done(function(goal){
      $('#name').text(goal.name);
      $('#area').text(goal.area);
      $('#type').text(goal.type);
      $('#description').text(goal.description);
      $('#status').text(goal.status);
      $('#update_news').text(goal.update_news);
      $('#percent_complete').css("width", goal.percent_complete+"%");
      $('#percent_complete').text(goal.percent_complete)
    });
  });
});
