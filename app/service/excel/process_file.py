def process_file(file_path: str, expected_headers: List[str]) -> bool:
    """
    Verifies the uploaded Excel file by checking its headers.

    Args:
        file_path (str): The path to the Excel file.
        expected_headers (List[str]): The list of expected headers.

    Returns:
        bool: True if the file is valid, False otherwise.
    """
    try:
        df = pd.read_excel(file_path)
        actual_headers = df.columns.tolist()
        return actual_headers == expected_headers
    except Exception as e:
        print(f"Error verifying file: {e}")
        return False
