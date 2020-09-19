function _(id){
	return document.getElementById(id);
}

// haystack (pagliaio), needle (ago) - cerca ago nel pagliaio
// cerca se una stringa contiene un'altra stringa

function contains(haystack,needle){
	return haystack.indexOf(needle)!==-1;
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

function is_localhost() {
	var current_url = window.location.href;
	return (contains(current_url, 'localhost') || contains(current_url, '127.0.0.1'));
}
