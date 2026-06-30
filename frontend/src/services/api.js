import axios from "axios";

const API = axios.create({
    baseURL: "https://hiresense-ai-a7q4.onrender.com"
});

export default API;