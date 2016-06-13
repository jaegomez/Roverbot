$(document).ready(function() {

	// When the forward button is clicked this code will execute
	$("#forward").mousedown(function() {
		// The API call to the robot to make it move forward should be made here
		console.log("moving forward");
		$.get("http://10.0.0.14:5000/movement?direction=forward", function(data){
			console.log(data);
		});
	})

	// This code gets executed when the forward button is released
	$("#forward").mouseup(function() {
		// The API call to the robot to make it STOP moving should be made here
		console.log("stoping");
		$.get("http://10.0.0.14:5000/stop", function(data){
			console.log(data);
		});
	})

	// When the backward button is clicked this will execute
	$("#backward").mousedown(function(){
		console.log("moving backwards");
		$.get("http://10.0.0.14:5000/movement?direction=backward", function(data){
			console.log(data);
		});
	})

	$("#backward").mouseup(function(){
		console.log("stoping");
		$.get("http://10.0.0.14:5000/stop", function(data){
			console.log(data);
		});
	})

	$("#left").mousedown(function(){
		console.log("moving Forward Left");
		$.get("http://10.0.0.14:5000/movement?direction=left", function(data){
			console.log(data);
		});
	})

	$("#left").mouseup(function(){
		console.log("stoping");
		$.get("http://10.0.0.14:5000/stop", function(data){
			console.log(data);
		});
	})

	$("#right").mousedown(function(){
		console.log("moving Forward right");
		$.get("http://10.0.0.14:5000/movement?direction=right", function(data){
			console.log(data);
		});
	})

	$("#right").mouseup(function(){
		console.log("stoping");
		$.get("http://10.0.0.14:5000/stop", function(data){
			console.log(data);
		});
	})

	$("#leftReverse").mousedown(function(){
		console.log("moving Backward Left");
		$.get("http://10.0.0.14:5000/movement?direction=leftreverse", function(data){
			console.log(data);
		});
	})

	$("#leftReverse").mouseup(function(){
		console.log("stoping");
		$.get("http://10.0.0.14:5000/stop", function(data){
			console.log(data);
		});
	})

	$("#rightReverse").mousedown(function(){
		console.log("moving Backward right");
		$.get("http://10.0.0.14:5000/movement?direction=rightreverse", function(data){
			console.log(data);
		});
	})

	$("#rightReverse").mouseup(function(){
		console.log("stoping");
		$.get("http://10.0.0.14:5000/stop", function(data){
			console.log(data);
		});
	})

	$("#StopButton").mouseup(function(){
		console.log("STOP");
		$.get("http://10.0.0.14:5000/stop?", function(data){
			console.log(data);
		});
	})
});
