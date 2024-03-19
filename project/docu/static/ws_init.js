let websocket; 

function ws_init(username)
{
	const base_url = window.location.protocol.replace('http', 'ws') + '//' +
		window.location.hostname + ":" + window.location.port;

	websocket = new WebSocket( base_url + '/ws/' + username + '/' )
	
	websocket.onopen = function(event){
		let data = localStorage.getItem("transcendence");
		data = JSON.parse(data);
		const logged = (data && data['access'] && data['refresh'] && data['username'])
		if (logged)
			console.log(data['username'], 'says connection opened');
		else
			console.log('unlogged client says connection opened');
		websocket.send("Client sends Welcome")
	}
	
	websocket.onmessage = function(event){
		console.log("message received: ", event)
		data = JSON.parse(event.data)
		console.log(event.data)
	}
	
	websocket.onclose = function(event){
		console.log('client says connection closed')
	}
}
	