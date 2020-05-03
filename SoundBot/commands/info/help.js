const { MessageEmbed, MessageAttachment } = require('discord.js');
module.exports = {
	name: "help",
	category:"info",
	description: "Returns the help string for the bot. This includes the list of active commands",
	usage: "\\help [args]",
	run: async (client, message, args) => {

		// This is the footer of every help message:
		const footer = "To learn more about SoundBot commands Type \\help <name of specific command(s)> or simply type \\help to list them all.";
		const embed_color = '#0099ff';
		const thumbnail_route = './../assets/soundbot_logo.png';
		const attachment = new MessageAttachment(thumbnail_route, 'soundbot_logo.png') 
		
		// Check for any positional arguments (i.e: if the user wants info on a specific command):
		if (Array.isArray(args) && args.length) {
			console.log("Arguments passed to help function:", args);
			
			let msg = await message.channel.send(`Here is info for these commands: ${args.toString()}`)
			// Try to parse the arguments if they are legitimate commands:
			for (let a of args) {
				if (client.commands.has(a)) {
					// Try to return an embed of the help string
					const helpstring = new MessageEmbed()
			    			.setColor(embed_color)
						//.attachFiles(thumbnail_route)
						//.setImage('attachment://soundbot_logo.png')
			    			.setTitle(`Usage for the ${a} command`)
			    			.addField('Description: ', client.commands.get(a).description, true)
			    			.addField('Usage: ',client.commands.get(a).usage, true)
			    			.setFooter(footer);
					
					message.channel.send({ embed: helpstring });
				}
				
				else {
					const helpstring = new MessageEmbed()
						.setColor(embed_color)
						//.attachFiles(thumbnail_route)
						//.setImage('attachment://soundbot_logo.png')
						.setTitle(`Usage for the ${a} command`)
						.addField(`Description: No command named ${a}`)
						.setFooter(footer);
				
					message.channel.send({ embed: helpstring });
				}
			}
		}

		// Otherwise, return the documentation for all the commands available to SoundBot:
		else {
			let msg = await message.channel.send('Here\'s a list of things you can ask me ...')
			const helpstring = new MessageEmbed()
				.setColor(embed_color)
				//.attachFiles(thumbnail_route)
				//.setImage('attachment://soundbot_logo.png')
				.setTitle('Soundbot Commands')
				.setFooter(footer);
			for (let c of client.commands.keys()) {
				helpstring.addField('Description:', client.commands.get(c).description, true);
				helpstring.addField('Usage', client.commands.get(c).usage, true);
				helpstring.addField('\u200B', '\u200b', false);
			}
			message.channel.send({ embed: helpstring });
		}
	}
}
