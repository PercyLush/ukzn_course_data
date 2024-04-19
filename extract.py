import pdfplumber
import os
import pandas as pd

def extract_tables_to_csv(pdf_path, start_page, end_page, output_folder):
    """
    Extracts tables from a specified range of pages in a PDF file and saves each table as a separate CSV file.

    :param pdf_path: Path to the PDF file.
    :param start_page: The starting page number for extraction.
    :param end_page: The ending page number for extraction.
    :param output_folder: Folder where the CSV files will be saved.
    """
    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(start_page - 1, end_page):  # Adjust for zero-based index
            page = pdf.pages[page_num]
            tables = page.extract_tables()

            for table_index, table in enumerate(tables):
                # Convert the table (a list of lists) into a pandas DataFrame
                df = pd.DataFrame(table[1:], columns=table[0])

                # Construct a filename for the CSV
                csv_filename = f"table_page_{page_num + 1}_table_{table_index + 1}.csv"
                csv_path = os.path.join(output_folder, csv_filename)

                # Save the DataFrame as a CSV file
                df.to_csv(csv_path, index=False)

                print(f"Saved table to {csv_path}")

# Example usage
pdf_path = "C:/Users/Bheki Lushaba/Downloads/college-of-law-and-management-studies-handbook-2020.pdf"
output_folder = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data"
start_page = 101
end_page = 103

if __name__ == "__main__":
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the output folder if it doesn't exist
    extract_tables_to_csv(pdf_path, start_page, end_page, output_folder)
