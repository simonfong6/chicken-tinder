// Functions.

// Determines whether the restaurant is displayed or not.
let restaurants_displayed = [];

function getRestaurants() {
  restaurants = $( ".restaurants" );
  return restaurants;
}


function initRestaurants(restaurants) {
  for (let i = 0; i < restaurants.length; i++) {
    restaurants_displayed.push(false);
  }
}

function updateRestaurantCards(restaurants) {
  for (let i = 0; i < restaurants.length; i++) {
    let restaurant = restaurants[i];
    let display = restaurants_displayed[i];

    if (display) {
      restaurant.style.display = "block";
    } else {
      restaurant.style.display = "none";
    }

  }
}

function findSetIndex() {
  for (let i = 0; i < restaurants_displayed.length; i++) {
    let displayed = restaurants_displayed[i];

    // Found the set one, return it.
    if (displayed) {
      return i;
    }
  }
}


function nextRestaurant() {
  let restaurants = getRestaurants();

  let setDisplay = false;
  for (let i = 0; i < restaurants_displayed.length; i++) {
    let displayed = restaurants_displayed[i];

    if (setDisplay) {
      restaurants_displayed[i] = true;
      break;
    }

    // Found the set one, need to set the next one in array.
    if (displayed) {
      setDisplay = true;
      restaurants_displayed[i] = false;
    }
  }

  updateRestaurantCards(restaurants);
}

function getRestaurantId(restaurant) {
  // Convert element to JQuery object. 
  let $restaurant = $(restaurant);
  
  // Get restaurant id stored in hidden input tag.
  let id = $restaurant.children().filter('#restaurant-id')[0].value;
  
  return id;
}

function disableButtons() {
  $('#reject').prop('disabled', true);
  $('#accept').prop('disabled', true);
}


function rejectRestaurant() {
  let restaurants = getRestaurants();
  let setIndex = findSetIndex();
  let numRestaurants = restaurants.length;
  let secondToLastRestaurantIndex = numRestaurants - 2;

  if (setIndex == secondToLastRestaurantIndex) {
    console.log("Last index, no more restaurants.");
    disableButtons();
  }

  console.log("Reject: " + setIndex);
  nextRestaurant();
}


function acceptRestaurant() {
  let restaurants = getRestaurants();
  let setIndex = findSetIndex();
  let numRestaurants = restaurants.length;
  let secondToLastRestaurantIndex = numRestaurants - 2;

  if (setIndex == secondToLastRestaurantIndex) {
    console.log("Last index, no more restaurants.");
    disableButtons();
  }

  let restaurant = restaurants[setIndex];

  let id = getRestaurantId(restaurant);

  socket.emit('accept', {'id': id, 'room': room})

  console.log("Accept: " + setIndex);

  nextRestaurant();
}

// Socket IO
let socket;

// Only run after the page setup.
$( document ).ready(function() {
  let restaurants = getRestaurants();

  initRestaurants(restaurants);

  updateRestaurantCards(restaurants);

  restaurants_displayed[0] = true;

  updateRestaurantCards(restaurants);

  // Hide match box.
  $('#match-box').hide();

  // Socket IO
  socket = io.connect('http://' + document.domain + ':' + location.port + '/matches');

  // When the socket connection is made, tell the server which room to join.
  socket.on('connect', function() {
    socket.emit('joined', {'room': room});
  });

  // Receive messages from the server.
  socket.on('status', function(data) {
    console.log(data.msg);
  });

  // Receive matches from the server.
  socket.on('match-found', function(data) {
    console.log("Matched restaurant: " + data.matched);
    // Show matched button!
    $('#match-box').show();
  });

});
