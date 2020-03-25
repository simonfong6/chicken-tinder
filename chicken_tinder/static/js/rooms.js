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


function rejectRestaurant() {
  let setIndex = findSetIndex();
  console.log("Reject: " + setIndex);
  nextRestaurant();
}


function acceptRestaurant() {
  let setIndex = findSetIndex();
  console.log("Accept: " + setIndex);

  nextRestaurant();
}

// Only run after the page setup.
$( document ).ready(function() {
  let restaurants = getRestaurants();

  initRestaurants(restaurants);

  updateRestaurantCards(restaurants);

  restaurants_displayed[0] = true;

  updateRestaurantCards(restaurants);

});