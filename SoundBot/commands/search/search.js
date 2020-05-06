const { MessageEmbed, MessageAttachment } = require('discord.js');
const { PythonShell } = require('python-shell');
function handleSearch(keyword) {
	var options = {
		mode: 'text',
		scriptPath:'/Users/davidlanday/Documents/soundBoard/SoundBot/scripts',
		args:[keyword]
	};
	// pythonPath:'../../../lib/python3.7',
	var list_sounds = new PythonShell('handleSearch.py', options);

	list_sounds.on('message', function (message) {
		console.log(JSON.parse(message))
	});
}
module.exports = {
	name: "search",
	category:"search",
	description: "Searches for a soundboard based on keyword arguments. If no argument is passed, a random soundboard is populated",
	usage: "\\search [args]",
	run: async (client, message, args) => {
		
		// If Keyword argument is given by user, then make the specified search:
		if (Array.isArray(args) && args.length == 1) {
			const msg = message.author.send(`Searching for sounboards related to ${args.toString()} ...`);
			
			// Show soundboards ...
		}
		else if (Array.isArray(args) && args.length > 1) {
			let query_w_spaces = args.toString().split(',').join(' ');
			message.author.send(`Searching for soundboards related to ${query_w_spaces} ...`);
		}
		else {
			message.author.send("Here\'s something you\'re really gonna like ...");
		}

		// Send search results to console:
		handleSearch(args);
	}
}
