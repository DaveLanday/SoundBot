// Load discord library:
const disc = require("discord.js");
const { config } = require("dotenv");

// Create a new bot/client:
const client = new disc.Client();

// Load token and prefix values from .env:
config({
	path: __dirname + "/.env"
});

// What happens when the bot starts?:
client.on("ready", () => { 
	console.log(`Bot launched. Hello, my name is ${client.user.username}. I pass butter and play soundboards.`);
	// client.user.setActivity(`Serving ${client.guilds.size} servers`);
});

// Login using bot creds:
client.login(process.env.API_KEY);
