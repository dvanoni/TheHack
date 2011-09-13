// Accelerometer vars
var ax = null, ay = null, az = null;

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

function sendData() {
	coords = getCoords();
	
	$.getJSON( '/api/recommend', { latitude: coords.latitude, longitude: coords.longitude }, function( data ) {
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