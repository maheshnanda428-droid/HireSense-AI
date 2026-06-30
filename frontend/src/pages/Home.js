import React, { useState } from "react";
import "./Home.css";
import API from "../services/api";

import Header from "../components/Header/Header";
import UploadBox from "../components/UploadBox/UploadBox";
import ScoreCard from "../components/ScoreCard/ScoreCard";
import SuggestionList from "../components/SuggestionList/SuggestionList";
import AIReport from "../components/AIReport/AIReport";
import Dashboard from "../components/Dashboard/Dashboard";
import ResumeRewrite from "../components/ResumeRewrite/ResumeRewrite";
import JobMatcher from "../components/JobMatcher/JobMatcher";
function Home() {

    const [score, setScore] = useState(null);
    const [suggestions, setSuggestions] = useState([]);
    const [resume, setResume] = useState(null);
    const [ai,setAi]=useState(null);
    const [resumeText, setResumeText] = useState("");
    const analyzeResume = async () => {

        if (!resume) {
            alert("Please upload a resume.");
            return;
        }

        try {

            const formData = new FormData();

            formData.append("file", resume);

            const response = await API.post("/upload", formData);

            setScore(response.data.score);
            setSuggestions(response.data.suggestions);
            setAi(response.data.ai);
            setResumeText(response.data.resume_text);
        } catch (error) {

            console.error(error);
            alert("Error analyzing resume.");

        }
    };

    return (

        <div className="home">

             <Dashboard>

            <Header />

            <UploadBox
                resume={resume}
                setResume={setResume}
                analyzeResume={analyzeResume}
            />

            <ScoreCard
                score={score}
            />

            <SuggestionList
                suggestions={suggestions}
            />

            <AIReport

ai={ai}

/>
<ResumeRewrite
ai={ai}
/>
<JobMatcher

    resumeText={resumeText}

/>
        </Dashboard>

</div>

    );

}

export default Home;