<!doctype html>
<html>
	<head>
		<meta charset="UTF-8" />
		<title>The Hack</title>	
		
		<!-- Apple iOS related stuffs -->
		<meta name="apple-mobile-web-app-status-bar-style" content="black" />
		<meta name="viewport" content="minimum-scale=1.0, width=device-width, maximum-scale=1">
		<meta name="apple-mobile-web-app-capable" content="YES">
		<link rel='apple-touch-icon' href='/static/img/touch-icon-iphone.png' />
		<link rel='apple-touch-icon' sizes='72x72' href='/static/img/touch-icon-ipad.png'/>
		<link rel='apple-touch-icon' sizes='114x114' href='/static/img/touch-icon-iphone4.png'/>
		<link rel='apple-touch-startup-image' href='/static/img/touch-startup.png' />
		
		<!-- jqTouch related stuffs -->
		<style type="text/css" media="screen">@import "/static/jqtouch/jqtouch.css";</style>
		<style type="text/css" media="screen">@import "/static/themes/apple/theme.css";</style>
		<style type="text/css" media="screen">@import "/static/extensions/jqt.bars/jqt.bars.css";</style>
		<style type="text/css" media="screen">@import "/static/extensions/jqt.bars/themes/apple/theme.css";</style>

		<!-- related stuffs -->
		<link rel="stylesheet" type="text/css" href="/static/css/master.css">
	</head>
	<body>
		<div id="tabbar"> 
			<div><ul> 
				<li> 
					<a href="#history" mask="/static/img/tabs/social.png" mask2x="/static/img/tabs/social.png"> 
						<strong>History</strong> 
					</a> 
				</li>
				<li> 
					<a href="#home" mask="/static/img/tabs/music.png" mask2x="/static/img/tabs/music.png"> 
						<strong>Music</strong> 
					</a> 
				</li> 
				<li> 
					<a onclick='loadSocial();' href="#social" mask="/static/img/tabs/social.png" mask2x="/static/img/tabs/social.png"> 
						<strong>Social</strong> 
					</a> 
				</li> 
			</ul></div> 
		</div>
		<div id='activity'>
			<div style='margin:16px 0;'><img src='/static/img/ajax-loader.gif'></div>
			<div>Loading...</div>
		</div>
		<div id="jqt">
			<div id='history'>
				<div class="toolbar">
					<h1>History</h1>
				</div>
				<div style='margin-top:44px;'>
					<ul class='edgetoedge'>
						<li class='sep'>Studying</li>
						<li>Test</li>
						<li>Test</li>
						<li>Test</li>
					</ul>
				</div>
			</div>
			<div id='social'>
				<div class="toolbar">
					<h1>Discover</h1>
					<div style='float:right;margin-top:-4px;'>
						<a onClick="window.location='https://www.facebook.com/dialog/oauth?client_id=170844926329169&amp;redirect_uri=http://thehack.dvanoni.com/api/facebook&amp;display=touch'"><img src="/static/img/facebook.png" width=32 height=32 style="vertical-align:middle;" /></a>
					</div>
				</div>
				<div style='margin-top:44px;'>
					<div id='discover-map-wrapper'>
						<img src='/static/img/staticmap.png'>
						<div id='discover-map' style='position:absolute;top:0;left:0;'></div>
					</div>					
					<div style='display:none;background-image:url(/static/img/staticmap.png);width:320px;height:460px;background-position:-160px -160px;'>
					</div>					
				</div>
			</div>
			<div id="home" class='current'>
				<div>
					<div id='artist-info'>
						<div>
							<div class='artist'>Artist Name</div>
							<div class='track'>Track Title</div>
						</div>
					</div>
					<div id='album-art-area'>
						<div id='next-album'>
							<img id='next' src='http://cdn.7static.com/static/img/sleeveart/00/007/786/0000778648_200.jpg' width='140' class='album-art'>
						</div>
						<div id='current-album'>
							<img id='current' src='http://cdn.7static.com/static/img/sleeveart/00/010/561/0001056176_200.jpg' width='240' class='album-art'>
						</div>
					</div>
				</div>
			</div>
		</div>
		<script src='/static/jqtouch/jquery-1.4.2.min.js' type='text/javascript'></script>
		<script src="/static/jqtouch/jqtouch.js" type="application/x-javascript" charset="utf-8"></script>
		<script src="/static/extensions/jqt.bars/jqt.bars.js" type="application/x-javascript" charset="utf-8"></script> 
		<script src="/static/js/geolocation.js" type='text/javascript' charset="utf-8"></script>
		<script src="/static/js/master.js" type='text/javascript' charset="utf-8"></script>
		<script type="text/javascript" charset="utf-8">
			function getRandomInt (min, max) {
		    	return Math.floor(Math.random() * (max - min + 1)) + min;
			}		
			
			function loadSocial() {
				$( '#activity' ).fadeIn( 'fast' );
				$( '#discover-map' ).html( '' ).scrollLeft( 80 ).scrollTop( 160 );
				
				$.getJSON( '/api/similar', null, function( data ) {
					for( var i = 0; i < data.length; i++ ) {
						var track = data[i];
						var top  = getRandomInt( 16, 578 );
						var left = getRandomInt( 16, 578 );
						
						if( track.album_img ) {
							var html = "<div class='social-track' style='top:" + top + "px;left:" + left + "px;'>" +
										"<img src='" + track.album_img + "' width='48'>" +
										"</div>";
							$( '#discover-map' ).append( html );
						}
					}
					
					$( '.social-track' ).fadeIn( 'slow' );
					$( '#activity' ).fadeOut( 'fast' );
				});				

			}
			
			$(function() {
				$.getJSON( '/front_end/dominant_color', { url: $( '#current' ).attr('src')}, function( color ) {
						$( '#home').css( 'background-color', color );
					});
					
				$( '#next' ).click( function() {
					$( '#activity' ).fadeIn( 'fast' );
					new_art = $( '#next' ).attr( 'src' )
					$( '#current' ).attr( 'src', new_art );
					$( '#next' ).attr( 'src', 'http://cdn.7static.com/static/img/sleeveart/00/008/225/0000822570_200.jpg' );
					
					$.getJSON( '/front_end/dominant_color', { url: $( '#current' ).attr('src')}, function( color ) {
							$( '#home').css( 'background-color', color );
							$( '#activity' ).fadeOut( 'fast' );
						});
					
				});
			});
		</script>
	</body>
</html>
