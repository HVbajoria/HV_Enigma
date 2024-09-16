import subprocess
import json

# Define the test cases
test_cases = [
    # Basic test cases
    {"filename": "basic_input_1.txt", "content": "5 3 2
1 3 10
2 4 20
3 5 15
", "output_filename": "basic_output_1.txt"},
    {"filename": "basic_input_2.txt", "content": "4 4 1
1 2 5
2 3 10
3 4 7
1 4 6
", "output_filename": "basic_output_2.txt"},
    {"filename": "basic_input_3.txt", "content": "3 3 2
1 2 10
2 3 20
1 3 15
", "output_filename": "basic_output_3.txt"},
    {"filename": "basic_input_4.txt", "content": "6 4 3
1 2 5
2 3 10
3 4 15
4 5 20
", "output_filename": "basic_output_4.txt"},

    # Corner test cases
    {"filename": "corner_input_1.txt", "content": "1 1 1
1 1 10
", "output_filename": "corner_output_1.txt"},
    {"filename": "corner_input_2.txt", "content": "10 5 2
1 10 100
1 5 50
6 10 60
2 7 70
3 8 80
", "output_filename": "corner_output_2.txt"},

    # Edge test cases
    {"filename": "edge_input_1.txt", "content": "100000 1 1
1 100000 1000000000
", "output_filename": "edge_output_1.txt"},
    {"filename": "edge_input_2.txt", "content": "100000 2 1
1 50000 1000000000
50001 100000 1000000000
", "output_filename": "edge_output_2.txt"},

    # Boundary test cases
    {"filename": "boundary_input_1.txt", "content": "2 2 1
1 1 10
2 2 20
", "output_filename": "boundary_output_1.txt"},
    {"filename": "boundary_input_2.txt", "content": "10 10 5
1 2 10
2 3 20
3 4 30
4 5 40
5 6 50
6 7 60
7 8 70
8 9 80
9 10 90
1 10 100
", "output_filename": "boundary_output_2.txt"}
]

# Write input files and run solution.py to generate output files
for test_case in test_cases:
    with open(test_case["filename"], 'w') as f:
        f.write(test_case["content"])

    # Run the solution.py script and capture the output
    result = subprocess.run(['python3', 'solution.py'], input=test_case["content"], text=True, capture_output=True)

    # Write the output to the corresponding output file
    with open(test_case["output_filename"], 'w') as f:
        f.write(result.stdout)

# Generate the JSON file containing all test cases in one line
with open('testcases.json', 'w') as f:
    json.dump(test_cases, f)

