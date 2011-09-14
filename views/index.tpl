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
			<div id='history'>
				<div class="toolbar">
					<h1>History</h1>
				</div>
				<div>
					<ul id='history-list' class='edgetoedge'>
						<!--<li class='sep'>Studying</li>
						<li>Test</li>
						<li>Test</li>
						<li>Test</li>-->
					</ul>
				</div>
			</div>
			<div id='social'>
				<div class="toolbar">
					<h1>Discover</h1>
				</div>
				<div>
					<div style='padding:8px;background: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#CCC), color-stop(0.6, #CCC), to(#AAA));'>
						<ul style='margin:0;'>
						%if login:
							<li><a onClick="window.location='https://www.facebook.com/dialog/oauth?client_id=170844926329169&redirect_uri=http://thehack.dvanoni.com/api/facebook&display=touch'"><img src="/static/img/facebook.png" width=50 height=50 style="vertical-align:middle;" />Connect with Facebook!</a></li>
						%else:
							<li><img src="{{fb_image}}" style="vertical-align:middle;" /> Welcome, {{username}}</li>
							%for artists in my_music["data"]:
								<li>{{artists["name"]}}</li>
								%end
						%end
						</ul>
					</div>
				</div>
			</div>
			<div id="home" class='current'>
				<div id='player'>
					<div id='player-audio'>
						<audio></audio>
					</div>
					<div id='player-track-info'>
						<div>
							<div class='artist'>Artist</div>
							<div class='title'>Title</div>
						</div>
					</div>
					<div id='player-album-art'>
						<div id='next-album'>
							<img alt='next album'/>
						</div>
						<div id='current-album'>
							<img alt='current album'/>
						</div>
					</div>
					<div id="player-controls">
						<button class="repeat">repeat is <span>OFF</span></button>
					</div>
				</div>
			</div>
		</div>
		<script src='/static/jqtouch/jquery-1.4.2.min.js' type='text/javascript'></script>
		<!--<script src="/static/js/jquery-ui-1.8.16.custom.min.js" type='text/javascript' charset="utf-8"></script>-->
		<script src="/static/jqtouch/jqtouch.js" type="application/x-javascript" charset="utf-8"></script>
		<script src="/static/extensions/jqt.bars/jqt.bars.js" type="application/x-javascript" charset="utf-8"></script> 
		<script src="/static/js/geolocation.js" type='text/javascript' charset="utf-8"></script>
		<script src="/static/js/player.js" type='text/javascript' charset="utf-8"></script>
		<script src="/static/js/master.js" type='text/javascript' charset="utf-8"></script>
		<script type="text/javascript">
			$(function() {
				sendData();
			});
		</script>
	</body>
</html>
