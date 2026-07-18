const express = require("express");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 8080;

const BACKEND_URL = process.env.BACKEND_URL || "http://localhost:5000";

app.use(express.static(path.join(__dirname, "public")));

app.get("/api/data", async (req, res) => {
  try {
    const response = await fetch(`${BACKEND_URL}/api/data`);
    const data = await response.json();
    res.json(data);
  } catch (err) {
    res.status(502).json({ error: "Could not reach backend", details: err.message });
  }
});

app.get("/health", (req, res) => {
  res.status(200).json({ status: "ok" });
});

app.listen(PORT, () => {
  console.log(`Frontend listening on port ${PORT}, backend at ${BACKEND_URL}`);
});