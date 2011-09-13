// Accelerometer vars
var ax = 0, ay = 0, az = 0;

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
		'/static/img/tabs/social.png',
	],
	useFastTouch: true
});

/*
	Send data that has been acquired from the phone to our API for 
	recommendations
*/
function sendData() {	
	// Mash all the phone data together
	coords = getCoords();	
	phone_data = {
		latitude: coords.latitude, 
		longitude: coords.longitude,
		accelerometer: ax + ',' + ay + ',' + az,
		timestamp: Date.now() / 1000.0
	};
	
	// Construct API call and work some magic
	$.getJSON( '/api/recommend', phone_data, function( data ) {
		console.log( data );
		
		var html = '';
		for( var i = 0; i < data.length; i++ ) {
			html += '<li class="arrow"><a href="#music-player">' + data[i].artist_name + ' - ' + data[i].title + '</a></li>'
		}
		
		$( '#playlist' ).html( html );
	});
}

$(function(){
	// Start acquiring our location
	acquireLocation();
	
	// Start grabbing accelerometer data
	if (typeof window.DeviceMotionEvent != 'undefined') {

		// Listen to motion events and update the position
		window.addEventListener('devicemotion', function (e) {
			ax = e.accelerationIncludingGravity.x;
			ay = e.accelerationIncludingGravity.y;
			az = e.accelerationIncludingGravity.z;
		}, false);
	}

	setTimeout( sendData, 2000 );
});