module.exports = {
	name: "ping",
	category:"info",
	description: "Testing whether bot is online and can be pinged",
	usage: "\\ping",
	run: async (client, message, args) => {
		const msg = await message.channel.send(`Pinging ...`);

		msg.edit(`Pong!\nLatency is ${Math.floor(msg.createdAt - message.createdAt)}ms\nAPI Latency is ${Math.round(client.ping)}ms`);
	}
}
