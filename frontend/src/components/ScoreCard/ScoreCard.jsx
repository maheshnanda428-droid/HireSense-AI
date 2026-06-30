import "./ScoreCard.css";

function ScoreCard({ score }) {

    if (score === null) return null;

    let status = "";
    let color = "";

    if (score >= 80) {
        status = "Excellent Resume";
        color = "#22C55E";
    }
    else if (score >= 60) {
        status = "Good Resume";
        color = "#EAB308";
    }
    else {
        status = "Needs Improvement";
        color = "#EF4444";
    }

    return (

        <div className="score-card">

            <h2>ATS SCORE</h2>

            <h1 style={{ color }}>{score}%</h1>

            <p>{status}</p>

            <div className="progress">

                <div
                    className="progress-fill"
                    style={{
                        width: `${score}%`,
                        background: color
                    }}
                ></div>

            </div>

        </div>

    );

}

export default ScoreCard;