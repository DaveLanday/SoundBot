// Load discord library:
const { Client, MessageEmbed, Collection } = require("discord.js");

// Load Configs:
const { config } = require("dotenv");

// Create a new bot/client:
const client = new Client();

// Get handler and events/commands:
client.commands = new Collection();
client.aliases = new Collection();

// Load token and prefix values from .env:
config({
	path: __dirname + "/.env"
});

// Load available commands:
['commands'].forEach(handler => {
	require(`./handler/${handler}`)(client);
});

// What happens when the bot starts?:
client.on('ready', () => { 
	console.log(`Bot launched. Hello, my name is ${client.user.username}. I pass butter and play soundboards.`);
	client.user.setPresence({
		status: 'online',
		game: {
			name: 'In Development',
			type: 'WATCHING'
		}
	});
});

client.on('message', async message => {
	
	// Define the command prefix:
	const prefix = "\\";

	if (message.author.bot) return;
	if (!message.guild) return;
	if (!message.content.startsWith(prefix)) return;
	if (!message.member) message.member = await message.guild.fetchMember(message);

	// Parse the input arguments:
	const args = message.content.slice(prefix.length).trim().split(/ +/g);
	const cmd = args.shift().toLowerCase();

	// Get the command based on the parsed arguments:
	let command = client.commands.get(cmd)
	if (!command){
		command = client.commands.get(client.aliases.get(cmd));
	}
	if (command) {
		command.run(client, message, args);
	}
});

// Login using bot creds:
client.login(process.env.API_KEY);
