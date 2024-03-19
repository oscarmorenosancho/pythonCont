function ws_init()
{
	const base_url = window.location.protocol.replace('http', 'ws') + '//' +
		window.location.hostname + ":" + window.location.port;

	const websocket = new WebSocket( base_url + '/ws/')
	
	websocket.onopen = function(event){
		console.log('client says connection opened')
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
	