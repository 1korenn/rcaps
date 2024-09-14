const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());

// Route to get insights
app.post('/get-insights', async (req, res) => {
    const userQuery = req.body.query;

    try {
        // Call your AI model here
        const response = await axios.post('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', {
            prompt: userQuery
        });

        // Return the AI response
        res.json({ insight: response.data.insight });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'An error occurred while fetching insights.' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
