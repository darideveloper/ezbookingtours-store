// Get wrapper of rthe iframe and delete content
const wrapper_iframe = document.querySelector (".et_pb_module.et_pb_sidebar_0_tb_body")
if (wrapper_iframe) {
  wrapper_iframe.innerHTML = ""
  
  // Get tour and location
  const tour_name = document.querySelector (".et_pb_text:nth-child(1) > div").innerHTML
  const tour_location = document.querySelector (".et_pb_text:nth-child(1) + div > div").innerHTML.split(": ")[1]
  
  // Generate url for iframe
  const host = "https://ezbookingtours-store.herokuapp.com/widget"
  const url  = `${host}/${tour_location}/${tour_name}`
  
  // Generate iframe and insert to wrapper
  const iframe = `<iframe src="${url}" width="300" height="800"></iframe>`
  wrapper_iframe.innerHTML = iframe
}