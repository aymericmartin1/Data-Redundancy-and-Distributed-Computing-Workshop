const express = require('express');
const app = express();
const PORT = 4000;

// The URL of the E-Commerce API
const SERVER_URL = 'localhost:5000';

app.get('/getServer', (req, res) => {
    res.json({ code: 200, server: SERVER_URL });
});

app.listen(PORT, () => {
    console.log(`The DNS Registry is running on http://localhost:${PORT}`);
});
