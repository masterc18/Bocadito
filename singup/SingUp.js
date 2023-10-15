const password = document.getElementById("password");
const show = document.getElementById("show1");

show.onchange = function (e) {
  password.type = show.checked ? "text" : "password";
};