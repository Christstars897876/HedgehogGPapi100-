const axios = require("axios");

async function sendMessage() {
  try {
    const response = await axios.post(
      "https://api.motadev.xyz/api/chat",
      {
        user_id: "UserID",
        messages: {
          system: "You are a sad ai",
          user: "Hello!"
        }
      },
      {
        headers: {
          "X-API-KEY": process.env.MOTADEV_API_KEY || "mtd_key1050789750IDEK",
          "User-Agent": "YourApp/1.0",
          "Referer": "https://api.motadev.xyz/auth/register",
          "Content-Type": "application/json"
        }
      }
    );

    console.log("Réponse de l'API :");
    console.log(response.data);
  } catch (error) {
    console.error("Erreur lors de la requête :");
    console.error(error.response?.data || error.message);
  }
}

sendMessage();

