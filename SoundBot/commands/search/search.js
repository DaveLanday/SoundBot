const { MessageEmbed, MessageAttachment } = require('discord.js');
const { PythonShell } = require('python-shell');
var board_list;
const embed_color = '#0099ff';
var page = 1;
function handleSearch(keyword, message) {
	var options = {
		mode: 'text',
		scriptPath:'/Users/davidlanday/Documents/soundBoard/SoundBot/scripts',
		args:[keyword]
	};
	
	// Trigger the python web-scraper:
	PythonShell.run('handleSearch.py', options, function (err,result) {
		console.log('finished');
		console.log(result);
		board_list = JSON.parse(result[0]);
		console.log(board_list);
		const total_pages = Object.keys(board_list).length;
		const search_results = new MessageEmbed();
	 	search_results.setColor(embed_color);
	 	search_results.setThumbnail(board_list[page-1]['img']);
		search_results.setTitle(board_list[page-1]['title']);
		search_results.addField('Options','Play Sound', true);
		search_results.setFooter(`Page ${page} of ${total_pages}`);
		message.author.send({ embed: search_results }).then(msg => {
			msg.react('👈').then( r => {
				msg.react('👉')
				msg.react('✅')

				const backFilter = (reaction,user) => reaction.emoji.name === '👈' && user.id === message.author.id;
				const forwardFilter = (reaction,user) => reaction.emoji.name === '👉' && user.id === message.author.id;
				const getSoundsFilter = (reaction, user) => reaction.emoji.name === '✅' && user.id === message.author.id;

				const back = msg.createReactionCollector(backFilter, { time: 600000 });
				const forward = msg.createReactionCollector(forwardFilter, { time: 600000 });
				const getSounds = msg.createReactionCollector(getSoundsFilter, {time: 600000});

				back.on('collect', r => {
					if (page === 1) {
						return;
					} 
					else {
						page--;
						search_results.setThumbnail(board_list[page-1]['img']);
						search_results.setTitle(board_list[page-1]['title']);
						search_results.setFooter(`Page ${page} of ${total_pages}`);
						msg.edit(search_results);
					} 
				});
				forward.on('collect', r => {
					if (page === total_pages) {						
						return;
					}
					else {
						page++;
                                                search_results.setThumbnail(board_list[page-1]['img']);
                                                search_results.setTitle(board_list[page-1]['title']);
						search_results.setFooter(`Page ${page} of ${total_pages}`);
                                                msg.edit(search_results)
					}
				});
				getSounds.on('collect', r => {
					search_results.setFooter('Press the ear to hear a sound');
					msg.reactions.removeAll().catch(error => console.error('Failed to clear reactions: ', error));
					msg.edit(search_results);
				});
			});
		});

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
			const msg = message.author.send(`Searching for soundboards related to ${args.toString()} ...`);
			
			// Show soundboards ...
		}
		else if (Array.isArray(args) && args.length > 1) {
			let query_w_spaces = args.toString().split(',').join(' ');
			message.author.send(`Searching for soundboards related to ${query_w_spaces} ...`);
		}
		else {
			message.author.send("Here\'s something you might like ...");
		}

		// Send search results to discord:
		handleSearch(args, message);
	}
}
console.log(board_list);
