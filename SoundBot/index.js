// Load discord library:
const disc = require("discord.js");

// Create a new bot/client:
const client = new disc.Client();

// Load token and prefix values from config.json:
const config = require("./config.json");

// What happens when the bot starts?:
client.on("ready", () => {
	console.log('Bot launched. It is being used by' ${client.users.size} 'in' ${client.channel.size} 'channels, in' ${client.guilds.size} ' guilds.');
	client.user.setActivity(`Serving ${client.guilds.size} servers`);
});
