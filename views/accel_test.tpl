<!doctype html>
<html>
<meta name="apple-mobile-web-app-status-bar-style" content="black" />
<script src='/static/jqtouch/jquery-1.4.2.min.js' type='text/javascript'></script>

<!-- 
<meta name="viewport" content="minimum-scale=1.0, width=device-width, maximum-scale=1">
<meta name="apple-mobile-web-app-capable" content="YES">
-->
<script type='text/javascript'>
	$( function() {
		document.ax = 0;
		document.ay = 0;
		document.az = 0;
		
		// Start grabbing accelerometer data
		if (typeof window.DeviceMotionEvent != 'undefined') {

			// Listen to motion events and update the position
			window.addEventListener('devicemotion', function (e) {
				delta_x = Math.abs( document.ax ) - Math.abs(  e.accelerationIncludingGravity.x );
				delta_y = Math.abs( document.ay ) - Math.abs(  e.accelerationIncludingGravity.y );
				delta_z = Math.abs( document.az ) - Math.abs(  e.accelerationIncludingGravity.z );
				
				document.ax = e.accelerationIncludingGravity.x;
				document.ay = e.accelerationIncludingGravity.y;
				document.az = e.accelerationIncludingGravity.z;

				$( '#accel' ).html( delta_x + '<br>' + delta_y + '<br>' + delta_z );
			}, false);
		}
	});
</script>
<body>
	<div id='accel'>
		adadf
	</div>
</body>
</html>