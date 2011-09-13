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
		
		<script src='/static/js/jquery-1.6.3.js' type='text/javascript'></script>
		<script src="/static/jqtouch/jqtouch.js" type="application/x-javascript" charset="utf-8"></script>
		<script src="/static/extensions/jqt.bars/jqt.bars.js" type="application/x-javascript" charset="utf-8"></script> 
		<script src="/static/js/wimf.js" type="application/x-javascript" charset="utf-8"></script> 
		
		<script type="text/javascript">
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
			<div id='details'>
				<div class="toolbar">
					<h1>Food Item</h1>
					<a href="#" id='info_back' class="back">Back</a>
				</div>
				<div class='s-scrollwrapper'>
					<div>
						<div style='padding:32px;background-color:#CCC;border-bottom:2px solid #333;border-top:2px solid #333;'>
							<table width='100%;'>
								<tr><td style='text-align:center;'>
									<img id='food-icon' src='/static/img/food/apple.png'>
								</td><td style='color:#333;'>
									<div id='food-name' style='font-size:16px;color:#1087be;margin-bottom:4px;font-weight:bold;'>
										<h1>Apple ( Fuji )</h1>
									</div>
									<div style='margin-bottom:4px;font-size:12px;'>
										<span style='font-weight:bold;'>Weight:</span> <span id='food-weight'>100.2g</span>
									</div>
								</td></tr>
							</table>
							<div style='text-align:center;'>
								<span id='food-age' style='color:#666;'>5 days old</span>
							</div>
						</div>
						<div style='padding:16px;'>
							<select class='grayButton' style='width:100%;height:48px;text-align:center;' onchange='changeType(this,document.selected_food.sensor,true);'>
								<option value='unknown'>Change Type</option>
								<optgroup label='Dairy'>
									<option value='milk'>Milk</option>
								</optgroup>
								<optgroup label='Fruits'>
									<option value='apple'>Apple</option>
									<option value='orange'>Orange</option>
								</optgroup>
								<optgroup label='Meat'>
									<option value='beef'>Beef</option>
									<option value='spam'>Spam</option>
								</optgroup>	
								<optgroup label='Veggies'>
									<option value='pepper'>Bell Pepper</option>
								</optgroup>
								<optgroup label='Misc'>
									<option value='wine'>Wine</option>
									<option value='beer'>beer</option>
									<option value='bread'>Bread</option>
									<option value='muffin'>Sweets</option>
									<option value='pizza'>Pizza</option>
								</optgroup>
							</select>
							<br/>
							<a href='#home' class='whiteButton' animation='slideright' onclick='remove_from_fridge();'>Remove from Fridge</a>
						</div>	
					</div>
				</div>
			</div>
			<div id='recipes'>
				<div class="toolbar">
					<h1>Recipe Search</h1>
				</div>
				<div class='s-scrollwrapper'>
					<div>
						<ul class="plastic">
							<li class="arrow">
							<a href="#my_ingredients">
								<table>
									<tr style="height:64px;"><td>
										<img height="64px" src='/static/img/genius.png'/>
									</td><td style='padding-left:16px;'>	
										Use My Ingredients
									</td></tr>
								</table>
								</a>
							</li>
							<li class="arrow">
							<a href="#recipe_search">
								<table>
									<tr><td>
										<img width="64px" src='/static/img/recipe.png'/>
									</td><td style='padding-left:16px;'>	
										Browse for Recipes
									</td></tr>
								</table>
								</a>
							</li>
						</ul>
					</div>
				</div>
			</div>	
			<div id='connect-details'>
				<div class="toolbar">
					<h1>Fridge Buddy</h1>
					<a href="#" class="back">Back</a>
				</div>
				<div class='s-scrollwrapper'>
					<div>
						<div class='info' style='padding:16px;border-bottom:2px solid #333;'>
							<div style='float:left;'>
								<img src='/static/img/friend.png'>
							</div>
							<div style='float:left; margin-left:16px;margin-top:16px;'>
								<div id='friend-name' style='font-size:20px;margin-bottom:4px;font-weight:bold;'>Andrew Huynh</div>
							</div>
							<div style='clear:both;line-height:0;'></div>
						</div>
						<h2>Let's Get Cookin'</h2>
						<div id='friend-recipes' style='height:1024px;'></div>
					</div>
				</div>
			</div>
			<div id='fridge-connect'>
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
			<div id='plan'>
				<div class="toolbar">
					<h1>Plan A Party</h1>
				</div>
				<div class='s-scrollwrapper'>
					<div>
						<div id='party-invitees'>
						</div>
						<div id='party-cat'>
							<div style='text-align:center;margin-top:32px;'>
								<div><img src='/static/img/party_cat.png'></div>
								<div>
									<h1 style='font-size:36px;'>Shake to party</h1>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div id="recipe_search">
				<div class="toolbar">
					<h1>Find a Recipe</h1>
					<a href="#home" class="back">Back</a>
				</div>
				<div class='s-scrollwrapper'>
					<div>
						<div style='padding:8px;background: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#CCC), color-stop(0.6, #CCC), to(#AAA));'>
							<ul style='margin:0;'>
								<li><input type="text" id="query" placeHolder="Search for a recipe!" onkeyup="searchRecipes(this)"></li>
							</ul>
						</div>
						<div id="search_results" style="height:1500px;"></div>
					</div>
				</div>
			</div>
			<div id="my_ingredients">
				<div class="toolbar">
					<h1>My Ingredients</h1>
					<a href="#home" class="back">Back</a>
				</div>
				<div class='s-scrollwrapper'>
					<div>
						<ul id="ingredient_list" class="rounded">
						</ul>
						<script type="text/javascript">
							$.getJSON('api/check_fridge.php', function(items) {
								for (i in items) {
									if( items[i].unknown ) {
										continue;
									}
									
									var ing = items[i].name;
									$('ul#ingredient_list').append(
										'<li><input type="checkbox" name="ingredient" value="' + ing + '" id="foo' + i + '"\/>'
										+ '<label class="checkbox_label" for="foo' + i + '">' + ing + '<\/label><\/li>');
								}
							});
						</script>
						<a style="margin:0 10px;color:rgba(0,0,0,.9)" href="recipe_search.php" onclick="set_search_params(this, false);" class="whiteButton">Find Recipes!</a>
					</div>
				</div>
			</div>
			<div id="home" class='current'>
				<div class="toolbar">
					<h1>The Hack</h1>
				</div>
				<div class="s-scrollwrapper">
					<div>
						<div id='fridge'>
							<div class='shelf'>
								<div id='shelf-1' class='shelf-padding'>
									<div id='1sp1' class='spot food-details'></div>
									<div id='1sp2' class='spot food-details'></div>
								</div>
							</div>
							<div class='shelf'>
								<div id='shelf-2' class='shelf-padding'>
									<div id='2sp1' class='spot food-details'></div>
									<div id='2sp2' class='spot food-details'></div>
								</div>
							</div>
							<div class='shelf'>
								<div id='shelf-3' class='shelf-padding'>
									<div id='3sp1' class='spot food-details'></div>
									<div id='3sp2' class='spot food-details'></div>
								</div>
							</div>
							<div class='shelf'>
								<div id='shelf-4' class='shelf-padding'>
									<div id='4sp1' class='spot food-details'></div>
									<div id='4sp2' class='spot food-details'></div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
