function food_details( sensor ) {
	var details = null;
	for( var i = 0; i < document.food_data.length; i++ ) {
		if( document.food_data[i].sensor == sensor ) {
			details = document.food_data[i];
			break;
		}
	}
	
	if( details == null ) {
		return;
	}
	
	document.selected_food = details;
	
	$('#food-name').html( details.name );
	$('#food-weight').html( details.weight + 'g' );
	$('#food-age').html( details.age );
	$('#food-icon').attr('src', 'img/food/' + details.icon + '.png' );
}

function addItem( spot, data ) {
	// TODO change this to have the correct info about the apple
	var food_item = '';
	if( !data.unknown ) {
		food_item = "<a class='food-details' style='display:none;' onclick='food_details(" + data.sensor + ");' href='#details'>" +
						"<div class='food' style='background:url(\"img/food/" + data.icon + ".png\");'><div class=\"lowfood\"> <img src=\"img/exclamation_point.png\"/></div></div>" +
					"</a>";
	} else {
		food_item = "<div class='food food-details' style='display:none;background:url(\"img/unknown-white.png\");'>" +
						"<select class='unknown' onchange='changeType(this," + data.sensor + ",false);'>" +
							"<option value='unknown'>Unknown</option>" +
							"<optgroup label='Dairy'>" +
								"<option value='milk'>Milk</option>" +
							"</optgroup>" +
							"<optgroup label='Fruits'>" +
								"<option value='apple'>Apple</option>" +
								"<option value='orange'>Orange</option>" +
							"</optgroup>" +
							"<optgroup label='Meat'>" +
								"<option value='beef'>Beef</option>" +
								"<option value='spam'>Spam</option>" +
							"</optgroup>" +							
							"<optgroup label='Veggies'>" +
								"<option value='pepper'>Bell Pepper</option>" +
							"</optgroup>" +
							"<optgroup label='Misc'>" +
								"<option value='wine'>Wine</option>" +
								"<option value='beer'>beer</option>" +
								"<option value='bread'>Bread</option>" +
								"<option value='muffin'>Sweets</option>" +
								"<option value='pizza'>Pizza</option>" +
							"</optgroup>" +
						"</select>" +
					"</div>";
	}
	
	$( '#' + spot ).html( food_item );
	$('.food-details').fadeIn('slow');
}
