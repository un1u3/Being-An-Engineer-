import json

try:
    # Read JSON file
    with open('test.json', 'r') as f:
        data = json.load(f)  # ✅ Correct JSON loading

    # Extract headers
    output = ','.join(data[0].keys())  # ✅ Extract column headers

    # Convert JSON to CSV
    for obj in data:
        output += f"\n{obj['Name']},{obj['age']},{obj['birthyear']}"  # ✅ Fixed f-string issue

    # Write CSV output
    with open('output.csv', 'w') as f:
        f.write(output)

    print("✅ CSV file saved successfully!")

except Exception as ex:
    print(f'Error: {str(ex)}')
