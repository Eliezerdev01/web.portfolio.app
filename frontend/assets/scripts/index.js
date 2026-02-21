function Drawer() {
  document.getElementById("drawer").classList.remove("hidden");
  document.getElementById("drawer").classList.add("visible");
}

function hide_drawer() {
    document.getElementById("drawer").classList.remove("visible");
    document.getElementById("drawer").classList.add("hidden");
;}

document.addEventListener('click', function (e) {
  const drawer = document.getElementById('drawer');
  if (e.target === drawer) {
    hide_drawer();
  }
});
function show_gallerry() {
  document.getElementById("gallery").classList.remove("hidden");
  document.getElementById("gallery").classList.add("visible");
};    