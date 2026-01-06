const API_URL = "https://nyxu41bkoc.execute-api.eu-north-1.amazonaws.com/prod";

async function fetchEvents() {
  const res = await fetch(`${API_URL}/events`);
  const data = await res.json();

  const eventsList = document.getElementById("events");
  eventsList.innerHTML = "";

  data.forEach(event => {
    const card = document.createElement("div");
    card.className = "event-card";

    card.innerHTML = `
      <h3>${event.title}</h3>
      <span>${event.eventDate}</span>
      <p>${event.description}</p>
    `;

    eventsList.appendChild(card);
  });
}

async function submitEvent() {
  const event = {
    title: document.getElementById("title").value,
    description: document.getElementById("description").value,
    eventDate: document.getElementById("eventDate").value,
    createdBy: "admin"
  };

  const res = await fetch(`${API_URL}/events`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(event)
  });

  const result = await res.json();
  document.getElementById("message").innerText = result.message;

  fetchEvents();
}

fetchEvents();
