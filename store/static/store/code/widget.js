// Get global inputs
const submit_button = document.querySelector('button[type="submit"]')

// Constrol variables for activate or deactivate submit button
let week_day_available = false

function validate_form () {
  // Validate form with inputs
  if (week_day_available && price > 0) {
    submit_button.disabled = false
  } else {
    submit_button.disabled = true
  }
}

function update_price () {
  // Update price of the tour (after changes in inputs for adults and childs)
  price = adults * adults_price + childs * childs_price
  document.querySelector('.price span').innerHTML = price
}


// Validate date of the week when change date
const week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
const week_days_spanish = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
const input_date = document.getElementById('date')
const input_date_error = document.querySelector ('#date + p')
input_date.addEventListener('change', function(e) {

  // Get date of the week
  const selected_date = new Date(input_date.value)
  const week_day_num = selected_date.getDay()
  const week_day = week_days[week_day_num]
  const week_day_spanish = week_days_spanish[week_day_num]
  week_day_available = days_available[week_day] == "True"

  // Show error message if date is not available
  if (week_day_available) {
    input_date_error.classList.add('d-none')
  } else {
    input_date_error.classList.remove('d-none')
    input_date_error.querySelector ("span").innerHTML = week_day_spanish
  }

  // Validate form after changes
  validate_form ()

})

// Detect event who change price
const input_adults = document.querySelector('.adults-wrapper input')
const decress_adults = document.querySelector('.adults-wrapper button:first-child')
const incress_adults = document.querySelector('.adults-wrapper button:last-child')
const input_childs = document.querySelector('.childs-wrapper input')
const decress_childs = document.querySelector('.childs-wrapper button:first-child')
const incress_childs = document.querySelector('.childs-wrapper button:last-child')
let adults = 1
let childs = 0

decress_adults.addEventListener('click', function(e) {
  // Decress number of adults for the tour
  if (adults > 1) {
    adults -= 1
    input_adults.value = adults
    update_price ()
    validate_form ()
  }
})

incress_adults.addEventListener('click', function(e) {
  // Incress number of adults for the tour
  adults += 1
  input_adults.value = adults
  update_price ()
  validate_form ()
})

decress_childs.addEventListener('click', function(e) {
  // Decress number of childs for the tour
  if (childs > 0) {
    childs -= 1
    input_childs.value = childs
    update_price ()
    validate_form ()
  }
})

incress_childs.addEventListener('click', function(e) {
  // Incress number of childs for the tour
  childs += 1
  input_childs.value = childs
  update_price ()
  validate_form ()
})

// Validate form when page load
validate_form ()

// Update price when page load
update_price ()