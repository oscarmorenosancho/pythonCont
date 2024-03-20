let myInterval;
let refreshTime = 240000;

SignupEl = document.getElementById("signupForm");
LoginEl = document.getElementById("loginForm");
RefreshEl = document.getElementById("refreshForm");
LogoutEl = document.getElementById("logoutForm");
UserBoxEl = document.getElementById("userbox");
UserDisplayEl = document.getElementById("userdisplay");

requestSignup = async (e) => {
	e.preventDefault()
	const data = {}
	const collection = e.target.getElementsByTagName("input");
	Array.prototype.slice.call(collection).forEach(element => {
			data[element.name] = element.value
		});
	url="/api/token/signup/"
	fetchPOST(url, data).then(async (content) => {
		Object.keys(content).forEach( (obkey) => {
		console.log(obkey, ":", content[obkey].toString())
		});
		if ( obkeys.includes('access') 
		&& obkeys.includes('refresh')
		&& obkeys.includes('username') )
		{
			localStorage.setItem("transcendence", 
				JSON.stringify({
					'access': content['access'],
					'refresh': content['refresh'],
					'username': content['username'],
				}));
		}
		else
			localStorage.removeItem("transcendence");
		e.target.reset();
		await refreshVisibility(false);
		myInterval = setInterval(requestRefresh, refreshTime);
	});
}

requestLogin = async (e) => {
	e.preventDefault()
	const data = {}
	const collection = e.target.getElementsByTagName("input");
	Array.prototype.slice.call(collection).forEach(element => {
			data[element.name] = element.value
		});
	url="/api/token/"
	fetchPOST(url, data).then(async (content) => {
		obkeys = Object.keys(content);
		obkeys.forEach( async (obkey) => {
		console.log(obkey, ":", content[obkey].toString())
		});
		if ( obkeys.includes('access') 
			&& obkeys.includes('refresh')
			&& obkeys.includes('username') )
		{
			localStorage.setItem("transcendence", 
				JSON.stringify({
					'access': content['access'],
					'refresh': content['refresh'],
					'username': content['username'],
				}));
			}
		else
			localStorage.removeItem("transcendence");
		e.target.reset();
		await refreshVisibility(false);
		myInterval = setInterval(requestRefresh, refreshTime);
	});
}

requestRefresh = async () => {
	data = localStorage.getItem("transcendence")
	data = JSON.parse(data);
	if (! data || !data['refresh'])
	{
		localStorage.removeItem("transcendence");
		return ;
	}
	data = { 'refresh': data['refresh']}
	url="/api/token/refresh/"
	fetchPOST(url, data).then(async (content) => {
		obkeys = Object.keys(content);
		obkeys.forEach( (obkey) => {
		console.log(obkey, ":", content[obkey].toString())
		});
		if ( obkeys.includes('access') 
			&& obkeys.includes('refresh')
			&& obkeys.includes('username') )
		{
			localStorage.setItem("transcendence", 
				JSON.stringify({
					'access': content['access'],
					'refresh': content['refresh'],
					'username': content['username'],
				}));
		}
		else
			localStorage.removeItem("transcendence");
		console.log('refreshed token')
		if (myInterval)
			clearInterval(myInterval);
		myInterval = setInterval(requestRefresh, refreshTime);
		await refreshVisibility(true);
	});
}

requestRefreshFromForm = async (e) =>
{
	e.preventDefault();
	requestRefresh();
}

requestLogout = async (e) => {
	e.preventDefault()
	let data = localStorage.getItem("transcendence")
	data = JSON.parse( data );
	let datasnd = JSON.stringify({ "disconnect": data.username });
	websocket.send( datasnd );
	if (! data || !data['access'])
	{
		localStorage.removeItem("transcendence");
		return ;
	}
	data = { 'access': data['access']}
	url="/api/token/logout/"
	fetchPOST(url, data).then(async (content) => {
		Object.keys(content).forEach( (obkey) => {
		console.log(obkey, ":", content[obkey].toString())
		});
		localStorage.removeItem("transcendence");
		await refreshVisibility(false);
		if (myInterval)
			clearInterval(myInterval);
	});
}

