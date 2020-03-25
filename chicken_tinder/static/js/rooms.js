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

// Only run after the page setup.
$( document ).ready(function() {
  restaurants = $( ".restaurants" );

  initRestaurants(restaurants);

  updateRestaurantCards(restaurants);

  restaurants_displayed[0] = true;

  updateRestaurantCards(restaurants);

});