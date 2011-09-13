var jQT = new $.jQTouch({
	icon: 'wimf-icon.png',
	addGlossToIcon: false,
	startupScreen: 'splashscreen.png',
	statusBar: 'black',
	preloadImages: [
		'/static/themes/jqt/img/back_button.png',
		'/static/themes/jqt/img/back_button_clicked.png',
		'/static/themes/jqt/img/button_clicked.png',
		'/static/themes/jqt/img/grayButton.png',
		'/static/themes/jqt/img/whiteButton.png',
		'/static/themes/jqt/img/loading.gif',
		'/static/img/tabs/refrigerator-tab.png',
		'/static/img/tabs/recipe.png',
		'/static/img/tabs/social.png',
		'/static/img/tabs/party.png',
		'/static/img/ajax-loader.gif'
	],
	useFastTouch: true
});

// Some sample Javascript functions:
$(function(){
	
	acquireLocation();
	
	// Grab accelerometer data
	if (typeof window.DeviceMotionEvent != 'undefined') {

		// Listen to motion events and update the position
		window.addEventListener('devicemotion', function (e) {
			x1 = e.accelerationIncludingGravity.x;
			y1 = e.accelerationIncludingGravity.y;
			z1 = e.accelerationIncludingGravity.z;
			console.log( x1 + ', ' + y1 + ', ' + z1 );
			
		}, false);
	}
	
	// Grab geolocation data
});