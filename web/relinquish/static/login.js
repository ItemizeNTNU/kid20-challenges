function login() {
	let password = document.querySelector("#password");
	const { MD5, SHA1, SHA256, SHA384, SHA512 } = CryptoJS;
	password.value = MD5(SHA1(SHA256(SHA384(SHA512(password.value)))));
	return true;
}
