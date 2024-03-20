from . import (
    convert_html_to_pdf,
    ai_generated_report
)
import asyncio
import time

# this should be the last piece you add
user_input = input("What would you like to generate a PDF report on?: ")

print("Generating Report, please wait...")
time.sleep(3)
print("AI is thinking, please wait...")


# user_input = "Write me a report on climate change, its effects and measures to control it."

ai_generated_report_html_str = ai_generated_report(user_input)

generated_pdf_file_name = asyncio.run(
    convert_html_to_pdf(html_string=ai_generated_report_html_str))
# print(generated_pdf_file_name)
# print(ai_generated_report_html_str)

print(f"Done... You can find your report at {generated_pdf_file_name}")
