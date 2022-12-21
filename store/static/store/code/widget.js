// Get global inputs
const submit_button = document.querySelector('button[type="submit"]')

// Constrol variables for activate or deactivate submit button
let week_day_available = false

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

function validate_form () {
  // Validate form with inputs
  if (week_day_available) {
    submit_button.disabled = false
  } else {
    submit_button.disabled = true
  }
}

// Validate form when page load
validate_form ()