function ResumeRewrite({ ai }) {

    if (!ai) return null;

    return (

        <div className="rewrite-card">

            <h2>✨ AI Resume Rewrite</h2>

            <p>

                {ai.resume_summary || "No rewritten summary available."}

            </p>

        </div>

    );

}

export default ResumeRewrite;