const { readdirSync, lstatSync } =  require('fs');

const ascii = require('ascii-table');

const command_table = new ascii('List of Commands').setHeading('Command', 'Load Status')

module.exports = (client) => {
	readdirSync('./commands/').forEach(dir => {
		
		// Only work on items that are directories:
		if (lstatSync('./commands/'+dir).isDirectory()) {
			const commands = readdirSync(`./commands/${dir}/`).filter(f =>f.endsWith('.js'));

			for (let file of commands) {
				let pull = require(`../commands/${dir}/${file}`);
				if (pull.name) {
					client.commands.set(pull.name, pull);
					command_table.addRow(file, 'yes');
				} else {
					command_table.addRow(file, 'no');
					continue;
				}

				if (pull.aliases && Array.isArray(pull.aliases)) {
					pull.aliases.forEach(alias => client.aliases.set(alias, pull.name));
				}
			}
		}
	});
	console.log(command_table.toString());
	console.log(client.commands.get('pong'));
}
