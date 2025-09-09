// Function to send the user's message and get a response from the backend
function sendMessage() {
  const userInput = document.getElementById("userInput").value.trim();
  if (userInput !== "") {
    displayMessage(userInput, "user"); // Display user's message

    // Make the API call to the Flask backend
    fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message: userInput,
      }),
    })
      .then(response => response.json())
      .then(data => {
        const chatbotResponse = data.response;
        displayMessage(chatbotResponse, "bot"); 
      })
      .catch(error => {
        console.error("Error:", error);
        displayMessage("I'm sorry, there was an error processing your request. Please try again.", "bot");
      });

    document.getElementById("userInput").value = "";
  }
}

function displayMessage(message, sender) {
  const chatBox = document.getElementById("chatBox");

  const messageDiv = document.createElement("div");
  messageDiv.classList.add("chat-message", sender);

 
  const avatarDiv = document.createElement("div");
  avatarDiv.classList.add("avatar");

 
  const avatarImage = document.createElement("img");
  avatarImage.src = sender === "user" ? "image/avatar1.jpg" : "image/avatar2.jpg"; // Add the respective icon paths
  avatarDiv.appendChild(avatarImage);


  const bubbleDiv = document.createElement("div");
  bubbleDiv.classList.add("chat-bubble");
  bubbleDiv.textContent = message;

  messageDiv.appendChild(avatarDiv);
  messageDiv.appendChild(bubbleDiv);


  chatBox.appendChild(messageDiv);


  chatBox.scrollTop = chatBox.scrollHeight;
}


document.getElementById("userInput").addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
    sendMessage();
  }
});

document.querySelector("button").addEventListener("click", function() {
  sendMessage();
});