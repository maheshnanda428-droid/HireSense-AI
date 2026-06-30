import "./UploadBox.css";

function UploadBox({ resume, setResume, analyzeResume }) {

    return (

        <div className="upload-container">

            <div className="upload-box">

                <h2>📄 Upload Resume</h2>

                <p>Choose a PDF Resume</p>

                <input
                    type="file"
                    accept=".pdf"
                    onChange={(e) => setResume(e.target.files[0])}
                />

                {

                    resume &&

                    <div className="selected-file">

                        ✅ {resume.name}

                    </div>

                }

                <button
                    onClick={analyzeResume}
                    className="upload-btn"
                >

                    🚀 Analyze Resume

                </button>

            </div>

        </div>

    );

}

export default UploadBox;