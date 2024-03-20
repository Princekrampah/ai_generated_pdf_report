import jinja2
import pdfkit


async def convert_html_to_pdf(
    html_string: str,
    template_folder: str = "./basics/templates",
    base_html_file: str = "base.html",
    output_file: str = "generate_pdf.pdf",
    output_folder: str = "./basics/generated_pdf_files",
) -> str:

    """
    Asynchronously converts an HTML file to a PDF file.

    This function takes the path of an HTML template file and generates a PDF file from it. The HTML file is expected to be located in the specified 'template_folder'. The generated PDF is saved with the name provided in 'output_file' and is stored in the specified 'output_folder'.

    Parameters:
    template_folder (str, optional): The path to the folder containing the HTML template. Defaults to "./templates".
    base_html_file (str, optional): The name of the base HTML file within the template folder. Defaults to "base.html".
    output_file (str, optional): The name of the output PDF file. Defaults to "generate_pdf.pdf".
    output_folder (str, optional): The path to the folder where the generated PDF file will be saved. Defaults to "../generated_pdf_files".

    Returns:
    str: The path to the generated PDF file.

    Note:
    - This function is asynchronous and should be awaited upon calling.
    - Ensure that the specified folders and files exist and are accessible.
    - The function might raise exceptions related to file reading/writing or PDF generation which should be handled appropriately.
    """

    if output_folder.endswith("/"):
        raise ValueError("Wrong output folder name, should not end with '/'")
    else:
        pdf_file_name = f"{output_folder}/{output_file}"

    try:
        template_loader = jinja2.FileSystemLoader(template_folder)
        template_env = jinja2.Environment(loader=template_loader)

        basic_template = template_env.get_template(base_html_file)

        output_html_code = basic_template.render()
        # print(output_html_code)

        # render content, this if for once we have AI generated response
        output_html_code = basic_template.render(
            ai_generated_content=html_string
        )

        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-bottom': '0.75in',
            'margin-right': '0.55in',
            'margin-left': '0.55in',
            'encoding': "UTF-8",
            'footer-right': '[page] of [topage]',
            'footer-font-size': "9",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'enable-local-file-access': False,
            'no-outline': None,
            'enable-local-file-access': False,
            'no-outline': None
        }

        pdfkit.from_string(
            input=output_html_code,
            output_path=pdf_file_name,
            options=options
        )

    except Exception as e:
        # good to log this exception instead
        print(e)
        return ""

    return pdf_file_name
