import "./SuggestionList.css";

function SuggestionList({ suggestions }) {

    if (!suggestions || suggestions.length === 0)
        return null;

    return (

        <div className="suggestion-card">

            <h2>💡 ATS Suggestions</h2>

            {

                suggestions.map((item, index) => (

                    <div
                        className="suggestion-item"
                        key={index}
                    >

                        <span className="tick">✓</span>

                        {item}

                    </div>

                ))

            }

        </div>

    );

}

export default SuggestionList;