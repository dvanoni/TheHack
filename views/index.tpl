<!doctype html>
<html>
	<head>
		<meta charset="UTF-8" />
		<title>The Hack</title>
		<meta name="apple-mobile-web-app-status-bar-style" content="black" />
		
		<style type="text/css" media="screen">@import "/static/jqtouch/jqtouch.css";</style>
		<style type="text/css" media="screen">@import "/static/themes/apple/theme.css";</style>
		<style type="text/css" media="screen">@import "/static/extensions/jqt.bars/jqt.bars.css";</style>
		<style type="text/css" media="screen">@import "/static/extensions/jqt.bars/themes/apple/theme.css";</style>
		<link rel="stylesheet" type="text/css" href="/static/css/master.css">
		<link rel="stylesheet" type="text/css" href="/static/css/ladl.css">
		
		<script src='/static/jqtouch/jquery-1.4.2.min.js' type='text/javascript'></script>
		<script src="/static/jqtouch/jqtouch.js" type="application/x-javascript" charset="utf-8"></script>
		<script src="/static/extensions/jqt.bars/jqt.bars.js" type="application/x-javascript" charset="utf-8"></script> 
		<script src="/static/js/wimf.js" type="application/x-javascript" charset="utf-8"></script> 
		
		<script type="text/javascript" charset='utf-8'>
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
				
				var i = document.createElement('input'); 
				alert( ('speech' in i || 'webkitSpeech' in i) );
			
				// Orientation callback event
				$('body').bind('turn', function(e, data){
					$('#orient').html('Orientation: ' + data.orientation);
				});
				
				if (typeof window.DeviceMotionEvent != 'undefined') {
					// Shake sensitivity (a lower number is more)
					var sensitivity = 20;

					// Position variables
					var x1 = 0, y1 = 0, z1 = 0, x2 = 0, y2 = 0, z2 = 0;

					// Listen to motion events and update the position
					window.addEventListener('devicemotion', function (e) {
						x1 = e.accelerationIncludingGravity.x;
						y1 = e.accelerationIncludingGravity.y;
						z1 = e.accelerationIncludingGravity.z;
					}, false);
				}
			});
		</script>
	</head>
	<body>
		<div id="tabbar"> 
			<div><ul> 
				<li> 
					<a href="#home" mask="/static/img/tabs/refrigerator-tab.png" mask2x="/static/img/tabs/refrigerator-tab.png"> 
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
		<div id="jqt">
			<div id='social'>
				<div class="toolbar">
					<h1>FridgeConnect</h1>
				</div>
				<div style='padding:8px;background: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#CCC), color-stop(0.6, #CCC), to(#AAA));'>
					<ul style='margin:0;'>
						<li><input type='text' onkeyup='searchFriends(this);' placeholder='Search for missing ingredients!'></li>
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
			<div id="music-player">
				<div class="toolbar">
					<h1>Music Player</h1>
					<a href="#home" class="back">Back</a>
				</div>
				<div class='s-scrollwrapper'>
					<div>
						Music player here
					</div>
				</div>
			</div>
			<div id="home" class='current'>
				<div class="toolbar">
					<h1>The Hack</h1>
				</div>
				<div class="s-scrollwrapper">
					<ul class="edgetoedge">
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
					</ul>
				</div>
			</div>
		</div>
	</body>
</html>
