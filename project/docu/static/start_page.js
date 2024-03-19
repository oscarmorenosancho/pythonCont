refreshVisibility = async () => 
{
	data = localStorage.getItem("transcendence")
	data = JSON.parse(data);
	const notlogged = (! data || !data['access'] || !data['refresh'] || !data['username'])
	SignupEl.style.display = !notlogged ? "none" : "block";
	LoginEl.style.display = !notlogged ? "none" : "block";
	RefreshEl.style.display = notlogged ? "none" : "block";
	LogoutEl.style.display = notlogged ? "none" : "block";
	UserBoxEl.style.display = notlogged ? "none" : "block";
	if (!data || !data['username'])
	{
		UserDisplayEl.innerText = "null";
		if (websocket)
		{
			websocket.close();
			websocket = undefined;
		}
	}
	else
	{
		const usrname = data['username']
		UserDisplayEl.innerText = usrname;
		ws_init(usrname);
	}
}

startPage = async (e) => {
	SignupEl.addEventListener("submit", requestSignup );
	LoginEl.addEventListener("submit", requestLogin );
	RefreshEl.addEventListener("submit", requestRefreshFromForm);
	LogoutEl.addEventListener("submit", requestLogout);

	await refreshVisibility();
}

startPage();