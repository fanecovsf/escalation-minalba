const popup = document.getElementById("popup");
const contactForm = document.getElementById("contactForm");

function openPopup() {
  popup.style.display = "block";
}

function closePopup() {
  popup.style.display = "none";
  contactForm.reset();
}

contactForm.addEventListener("submit", function(event) {
  event.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const phone = document.getElementById("phone").value;

  const contact = {
    name: name,
    email: email,
    phone: phone,
  };

  // You can perform further actions with the contact data, like adding to a list or sending to a server.
  console.log("New contact:", contact);

  closePopup();
});