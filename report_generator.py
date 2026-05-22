import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)
from reportlab.lib import styles
from reportlab.lib.styles import getSampleStyleSheet

try:
    # Read CSV file
    df = pd.read_csv("sales_data.csv")

    print("Dataset Loaded Successfully\n")
    print(df)

    # Analysis
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()

    best_product = df.loc[df["Sales"].idxmax(), "Product"]

    print("\nAnalysis Completed")

    # Create graph
    plt.figure(figsize=(8,5))
    plt.bar(df["Product"], df["Sales"])

    plt.title("Sales by Product")
    plt.xlabel("Products")
    plt.ylabel("Sales")

    plt.xticks(rotation=20)

    plt.tight_layout()

    plt.savefig("sales_chart.png")

    plt.close()

    print("Chart Created")

    # Create PDF report
    doc = SimpleDocTemplate("sales_report.pdf")

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        "Automated Sales Report",
        styles['Title']
    )

    story.append(title)

    story.append(Spacer(1,20))

    summary = f"""
    Total Sales: {total_sales}<br/>
    Total Profit: {total_profit}<br/>
    Best Selling Product: {best_product}
    """

    story.append(
        Paragraph(summary, styles['BodyText'])
    )

    story.append(Spacer(1,20))

    img = Image(
        "sales_chart.png",
        width=400,
        height=250
    )

    story.append(img)

    doc.build(story)

    print("\nPDF Report Generated Successfully")

except Exception as e:
    print("Error:", e)