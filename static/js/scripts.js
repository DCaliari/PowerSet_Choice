function slider_update_value(image, id_image_value) {
	var slider = document.getElementById(image);
	var output = document.getElementById(id_image_value);
	output.innerHTML = slider.value;

	slider.oninput = function() {
		output.innerHTML = this.value;
	}
}

