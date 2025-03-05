const express = require('express');
const app = express();
const PORT = 4000;

// The URL of the Hello World server
const SERVER_URL = 'localhost:3001';

app.get('/getServer', (req, res) => {
    res.json({ code: 200, server: SERVER_URL });
});

app.listen(PORT, () => {
    console.log(`The DNS Registry is running on http://localhost:${PORT}`);
});
