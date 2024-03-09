document.addEventListener("DOMContentLoaded", function () {
  const passwordInput = document.getElementById("password");
  const showPassword = document.getElementById("show");
  const bread = document.querySelector("#Bread");
  const phrase = document.querySelector("#card");
  showPassword.addEventListener("change", function () {
    if (this.checked) {
      passwordInput.type = "text";
    } else {
      passwordInput.type = "password";
    }
  });
  bread.addEventListener("click", () => {
    phrase.classList.add("show");
  });

  bread.addEventListener("click", () => {
    phrase.classList.remove("show");
  });
});
