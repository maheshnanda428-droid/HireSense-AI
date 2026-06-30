from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(data):

    doc = SimpleDocTemplate("report.pdf")

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>HireSense AI Report</b>", styles["Title"]))

    elements.append(
        Paragraph(
            f"ATS Score: {data['score']}",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            data["ai"]["overall_evaluation"],
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            "<b>Strengths</b>",
            styles["Heading2"]
        )
    )

    for item in data["ai"]["strengths"]:

        elements.append(
            Paragraph(item, styles["BodyText"])
        )

    elements.append(
        Paragraph(
            "<b>Weaknesses</b>",
            styles["Heading2"]
        )
    )

    for item in data["ai"]["weaknesses"]:

        elements.append(
            Paragraph(item, styles["BodyText"])
        )

    doc.build(elements)

    return "report.pdf"