import chardet

def detect_encoding(file_path):
    # Open the file in binary mode ('rb') to read its content
    with open(file_path, 'rb') as file:
        # Use chardet to detect the encoding of the file content
        result = chardet.detect(file.read())

        # Retrieve the detected encoding and confidence level
        encoding = result['encoding']
        confidence = result['confidence']

    # Return the detected encoding and confidence level
    return encoding, confidence

# Replace 'seu_arquivo.txt' with the path of the file you want to check
file_path = 'C:\\Users\\ernes\\Downloads\\id,rubrica,mes,valor,ano.txt'

# Call the detect_encoding function to get the encoding and confidence of the file
encoding, confidence = detect_encoding(file_path)

# Print the results
print(f'The encoding of the file {file_path} is {encoding} with a confidence of {confidence:.2f}')
