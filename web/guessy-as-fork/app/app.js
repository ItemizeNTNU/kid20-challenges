const fs = require('fs');
const polka = require('polka');

const speeding = fs.readFileSync('speeding.jpg');

const reqs = {};

const MAX_REQUESTS = 10000;
const MAX_TIME = 1 * 60 * 1000;

function redirect(res, location) {
	let str = `Redirecting to ${location}`;
	res.writeHead(302, {
		Location: location,
		'Content-Type': 'text/plain',
	});
	res.end(str);
};

const stats = {
	'/e73470324687126d04a9386831482ff7/flag.txt': 200
};

const blockRoute = polka({
	onNoMatch: (req, res) => {
		redirect(res, '/waf/error/speeding');
	}
});

blockRoute.get('/waf/', (req, res) => {
	res.end('Unknown action, use one of the following: error, statistics');
});

blockRoute.get('/waf/error/', (req, res) => {
	res.end('Unknown error, use one of the following: speeding');
});

blockRoute.get('/waf/error/speeding', (req, res) => {
	res.writeHead(200, { 'Content-Type': 'image/jpeg' });
	res.end(speeding);
});

blockRoute.get('/waf/statistics/', (req, res) => {
	res.end('Unknown statistic, use one of the following: access');
});

blockRoute.get('/waf/statistics/access', (req, res) => {
	const data = JSON.stringify(stats, Object.keys(stats).sort());
	res.writeHead(200, {
		'Content-Type': 'application/json;charset=utf-8',
	});
	res.end(data);
});

function waf(req, res, next) {
	res.removeHeader('Date');
	if (!req.path.startsWith('/e73470324687126d04a9386831482ff7/flag.txt')) {
		stats[req.path] = 404;
	}
	const ip = req.connection.remoteAddress;
	if (!reqs[ip]) {
		reqs[ip] = [];
	}
	let access = reqs[ip];
	const now = new Date().getTime();
	let i = 0;
	for (; i < access.length; i++) {
		const time = access[i];
		if (time > now) {
			break;
		}
	}
	if (i > 0) {
		access = access.slice(i, access.length);
		reqs[ip] = access;
	}
	if (access.push(now + MAX_TIME) > MAX_REQUESTS) {
		blockRoute.handler(req, res);
		return;
	}
	next();
}

const app = polka();
app.use(waf);
app.get('/', (req, res) => {
	res.end('Hi there, nothing special at this place. Maybe try somewhere else?');
});
app.get('/e73470324687126d04a9386831482ff7/flag.txt', (req, res) => {
	res.end('KID20{tOlD_Y0u_n0t_6U3zzy}');
});
app.listen(3000, err => {
	if (err) throw err;
	console.log(`> Running on localhost:3000`);
});
