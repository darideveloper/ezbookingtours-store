// Nodes
const input_adults = document.querySelector('.adults-wrapper input')
const decress_adults = document.querySelector('.adults-wrapper button:first-child')
const incress_adults = document.querySelector('.adults-wrapper button:last-child')
const input_childs = document.querySelector('.childs-wrapper input')
const decress_childs = document.querySelector('.childs-wrapper button:first-child')
const incress_childs = document.querySelector('.childs-wrapper button:last-child')

const input_date = document.getElementById('date')
const input_date_error = document.querySelector ('#date + p')

const input_time = document.getElementById('time')
const input_hotel = document.getElementById('hotel')

const submit_button = document.querySelector('button[type="submit"]')

// Update functions

function update_price () {
  // Update price of the tour (after changes in inputs for adults and childs)
  price = adults * adults_price + childs * childs_price
  document.querySelector('.price span').innerHTML = price
}

function update_hotels () {
  // Get time
  time = input_time.value

  // get hootel options
  const available_hotels = hotels.filter ((hotel) => hotel.tour_time == time)
  input_hotel.innerHTML = ''

  // Set hotel options
  available_hotels.forEach(hotel => {
    const option = document.createElement('option')
    option.value = hotel.id
    option.innerHTML = hotel.hotel
    input_hotel.appendChild(option)
  })  
}

function update_pick_up () {
  // Get hotel data
  const hotel_id = input_hotel.value
  const hotel = hotels.find ((hotel) => hotel.id == hotel_id)
  
  // Update pick up time
  document.querySelector('.pick-up span').innerHTML = hotel.pick_up
}

// DATES

// Validate date of the week when change date
const week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
const week_days_spanish = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
input_date.addEventListener('change', function(e) {

  // Get date of the week
  const selected_date = new Date(input_date.value)
  const week_day_num = selected_date.getDay()
  const week_day = week_days[week_day_num]
  const week_day_spanish = week_days_spanish[week_day_num]
  const week_day_available = days_available[week_day] == "True"

  // Show error message if date is not available
  if (week_day_available) {

    // Hide error message
    input_date_error.classList.add('d-none')

    // Activate submit button
    submit_button.disabled = false
  } else {
    // Show error message
    input_date_error.classList.remove('d-none')
    input_date_error.querySelector ("span").innerHTML = week_day_spanish

    // Deactivate submit button
    submit_button.disabled = true
  }
})

// PRICE

// Detect event who change price
let adults = 1
let childs = 0

decress_adults.addEventListener('click', function(e) {
  // Decress number of adults for the tour
  if (adults > 1) {
    adults -= 1
    input_adults.value = adults
    update_price ()
  }
})

incress_adults.addEventListener('click', function(e) {
  // Incress number of adults for the tour
  adults += 1
  input_adults.value = adults
  update_price ()
})

decress_childs.addEventListener('click', function(e) {
  // Decress number of childs for the tour
  if (childs > 0) {
    childs -= 1
    input_childs.value = childs
    update_price ()
  }
})

incress_childs.addEventListener('click', function(e) {
  // Incress number of childs for the tour
  childs += 1
  input_childs.value = childs
  update_price ()
})

// HOTELS

// Update hotels (and pick ups) options after change the time
input_time.addEventListener('change', function(e) {
  if (input_hotel) {
    update_hotels ()
    update_pick_up ()
  }
})

// PICK UP

// Update pick up time after change the hotel, if hotel input exist
if (input_hotel) { 
  input_hotel.addEventListener('change', function(e) {
    update_pick_up ()
  })
}

// Show spinner when submit form
document.querySelector('form').addEventListener('submit', function(e) {
  document.querySelector('.wrapper-spinner').classList.remove('d-none')
})

// ON LOAD  

// Update price when page load
update_price ()

// Validate if hotel input exist
if (input_hotel) {
  // Update hotels options when page load
  update_hotels ()  
  
  // Update pick up when page load
  update_pick_up ()

} else {
  // Delete pick up date if hotel input not exist
  document.querySelector('.pick-up').classList.add("d-none")
  document.querySelector('label[for="hotel"]').classList.add('d-none')
}