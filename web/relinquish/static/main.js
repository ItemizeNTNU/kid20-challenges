fetch('/api/active/5')
	.then(data => {
		return data.json()
	})
	.then(json => {
		const node = document.querySelector("#active");
		node.innerHTML = "";
		json.forEach(user => {
			const el = document.createElement("p");
			el.innerText = `${user.username}: ${user.last_active} minutes ago`
			node.appendChild(el);
		});
	})
	.catch(err => {
		console.log("Error loading active users:", err)
		document.querySelector("#active").textContent = "Error loading last active users.";
	})