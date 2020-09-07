function _(id){
	return document.getElementById(id);
}

/* View in fullscreen */
function openFullscreen() {
	/* Get the element you want displayed in fullscreen mode (a video in this example): */
	var elem = document.documentElement;

	if (elem.requestFullscreen) {
		elem.requestFullscreen();
	} else if (elem.mozRequestFullScreen) { /* Firefox */
		elem.mozRequestFullScreen();
	} else if (elem.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
		elem.webkitRequestFullscreen();
	} else if (elem.msRequestFullscreen) { /* IE/Edge */
		elem.msRequestFullscreen();
	}
}

// These functions regards the drag and drop of the images
function allowDrop(ev) {
	ev.preventDefault();
}

function drag(ev) {
	ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
	ev.preventDefault();
	var data = ev.dataTransfer.getData("text");
	if(data==="" || data==="\r\n") {
		return;
	}
	var data_obj = document.getElementById(data);
	console.log(data_obj);
	ev.target.appendChild(data_obj);
}

function slider_update_value(image, id_image_value) {
	var slider = document.getElementById(image);
	var output = document.getElementById(id_image_value);
	output.innerHTML = slider.value;

	slider.oninput = function() {
		output.innerHTML = this.value;
	}
}