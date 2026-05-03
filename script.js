
let contacts = JSON.parse(localStorage.getItem("contacts")) || [];

function saveData() {
  localStorage.setItem("contacts", JSON.stringify(contacts));
}

function displayContacts(data = contacts) {
  const list = document.getElementById("list");
  list.innerHTML = "";

  data.forEach((c, index) => {
    list.innerHTML += `
      <div class="contact">
        <div>
          <strong>👤 ${c.name}</strong><br>
          📞 ${c.phone}
        </div>
        <span class="delete" onclick="deleteContact(${index})">❌</span>
      </div>
    `;
  });
}

function addContact() {
  const name = document.getElementById("name").value;
  const phone = document.getElementById("phone").value;

  if (name === "" || phone === "") {
    alert("Fill all fields!");
    return;
  }

  contacts.push({ name, phone });
  saveData();
  displayContacts();

  document.getElementById("name").value = "";
  document.getElementById("phone").value = "";
}

function deleteContact(index) {
  contacts.splice(index, 1);
  saveData();
  displayContacts();
}

function searchContact() {
  const value = document.getElementById("search").value.toLowerCase();
  const filtered = contacts.filter(c =>
    c.name.toLowerCase().includes(value)
  );
  displayContacts(filtered);
}

// LOAD ON START
displayContacts();
