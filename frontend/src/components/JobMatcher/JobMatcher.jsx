import { useState } from "react";
import API from "../../services/api";
import "./JobMatcher.css";

function JobMatcher({ resumeText }) {

    const [jd, setJd] = useState("");
    const [result, setResult] = useState(null);

    const analyze = async () => {

        if (!resumeText) {
            alert("Analyze your resume first.");
            return;
        }

        if (!jd.trim()) {
            alert("Paste the Job Description.");
            return;
        }

        const response = await API.post("/job-match", {

            resume_text: resumeText,

            job_description: jd

        });

        setResult(response.data);

    };

    return (

        <div className="job-card">

            <h2>🎯 Job Description Match</h2>

            <textarea

                rows="8"

                placeholder="Paste Job Description..."

                value={jd}

                onChange={(e)=>setJd(e.target.value)}

            />

            <button onClick={analyze}>

                Analyze Match

            </button>

            {

                result &&

                <>

                    <h3>

                        Match Score

                    </h3>

                    <h1>

                        {result.match_score}%

                    </h1>

                    <h3>

                        Missing Skills

                    </h3>

                    <ul>

                        {

                            result.missing_skills.map(

                                (item,index)=>

                                <li key={index}>{item}</li>

                            )

                        }

                    </ul>

                </>

            }

        </div>

    );

}

export default JobMatcher;