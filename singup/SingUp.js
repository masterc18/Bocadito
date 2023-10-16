const password = document.getElementById("password");
const show = document.getElementById("show1");

show.onchange = function (e) {
  password.type = show.checked ? "text" : "password";
};

const password2 = document.getElementById("password2");
const show2 = document.getElementById("show2");

show2.onchange = function (e) {
  password2.type = show2.checked ? "text" : "password";
};
