import "./AIReport.css";

function AIReport({ ai }) {

    if (!ai) return null;

    return (

        <div className="ai-report">

            <h2>🤖 AI Resume Evaluation</h2>

            <h3>Overall Evaluation</h3>

            <p>{ai.overall_evaluation || "No evaluation available."}</p>

            <h3>💪 Strengths</h3>

            <ul>
                {(ai.strengths || []).map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>

            <h3>⚠️ Weaknesses</h3>

            <ul>
                {(ai.weaknesses || []).map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>

            <h3>💡 Recommendations</h3>

            <ul>
                {(ai.recommendations || []).map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>

            <h3>🎤 Interview Questions</h3>

            <ol>
                {(ai.interview_questions || []).map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ol>

        </div>

    );

}

export default AIReport;