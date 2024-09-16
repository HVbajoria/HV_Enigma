from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str, input2: str, input3: str, input4:str, input5:str) -> str:
    f = open("demo.txt", "a")
    f.write(input5 + "\n\n" + input1 + "\n\n" + input2 + "\n\n" + input3 + "\n\n" + "\n\n" +"### Program to generate testcases:\n\n"+ input4)
    f.close()
    return input5 + "\n\n" + input1 + "\n\n" + input2 + "\n\n" + input3 + "\n\n" + "\n\n" +"### Program to generate testcases:\n\n"+ input4