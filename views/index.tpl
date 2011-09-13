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
						<li><a href="https://www.facebook.com/dialog/oauth?client_id=170844926329169&redirect_uri=thehack.dvanoni.com/api/facebook&scope=user_likes&display=touch">Connect with Facebook</a></li>
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
					<ul id='playlist' class="edgetoedge">
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
						<li class="arrow"><a href="#music-player">Test</a></li>
					</ul>
				</div>
			</div>
		</div>
		<script src='/static/jqtouch/jquery-1.4.2.min.js' type='text/javascript'></script>
		<script src="/static/jqtouch/jqtouch.js" type="application/x-javascript" charset="utf-8"></script>
		<script src="/static/extensions/jqt.bars/jqt.bars.js" type="application/x-javascript" charset="utf-8"></script> 
		<script src="/static/js/geolocation.js" type='text/javascript' charset="utf-8"></script>
		<script src="/static/js/master.js" type='text/javascript' charset="utf-8"></script>
	</body>
</html>
