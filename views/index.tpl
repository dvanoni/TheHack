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
					<a href="#social" mask="/static/img/tabs/social.png" mask2x="/static/img/tabs/social.png"> 
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
			<div id='social'>
				<div class="toolbar">
					<h1>SongConnect</h1>
				</div>
				<div style='padding:8px;background: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#CCC), color-stop(0.6, #CCC), to(#AAA));'>
					<ul style='margin:0;'>
						<li><input type='text' onkeyup='searchFriends(this);' placeholder='Search for missing ingredients!'></li>
					</ul>
				</div>
				<div style='padding:8px;background: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#CCC), color-stop(0.6, #CCC), to(#AAA));'>
					<ul style='margin:0;'>
%if login:
						<li><a onClick="window.location='https://www.facebook.com/dialog/oauth?client_id=170844926329169&redirect_uri=http://thehack.dvanoni.com/api/facebook&display=touch'">Connect with Facebook</a></li>
%else:
						<li><img src="{{fb_image}}" style="vertical-align:middle;" /> Welcome, {{username}}</li>
%end
					</ul>
				</div>
				<div class='s-scrollwrapper'>
					<div>
						<div style='height:420px;'>
							<ul id='friends' class="plastic"></ul>
						</div>
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
							<img id='next' src='http://farm7.static.flickr.com/6204/6144054545_0620580270.jpg' width='140' class='album-art'>
						</div>
						<div id='current-album'>
							<img id='current' src='http://farm7.static.flickr.com/6064/6139558300_2cab708c94.jpg' width='240' class='album-art'>
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
			$(function() {
				$.getJSON( '/front_end/dominant_color', { url: $( '#current' ).attr('src')}, function( color ) {
						$( '#home').css( 'background-color', color );
					});
				
				$( '#next' ).click( function() {
					$( '#activity' ).fadeIn( 'fast' );
					new_art = $( '#next' ).attr( 'src' )
					$( '#current' ).attr( 'src', new_art );
					$( '#next' ).attr( 'src', 'http://1.bp.blogspot.com/_WC5D7MIXrq8/TRRPP8Qz23I/AAAAAAAAAME/1sXt_IUQwUE/s640/black.square.jpg' );
					
					$.getJSON( '/front_end/dominant_color', { url: $( '#current' ).attr('src')}, function( color ) {
							console.log( color );
							$( '#home').css( 'background-color', color );
							$( '#activity' ).fadeOut( 'fast' );
						});
					
				});
			});
		</script>
	</body>
</html>
