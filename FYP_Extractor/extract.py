import re

# Read the text file
with open('FYP_Extractor\MESI-2.txt', 'r') as file:
    data = file.read()

# # Use regular expression to find the numbers following the string
matches = re.findall(r'L1Dcache\.m_demand_misses\s+(\d+)', data)

# # Extracted numbers
numbers = [int(match) for match in matches]


print(sum(numbers))


with open('FYP_Extractor\MESI-4.txt', 'r') as file:
    data = file.read()

# # Use regular expression to find the numbers following the string
matches = re.findall(r'L1Dcache\.m_demand_misses\s+(\d+)', data)


# # Extracted numbers
numbers = [int(match) for match in matches]


print(sum(numbers))

with open('FYP_Extractor\MESI-8.txt', 'r') as file:
    data = file.read()

# # Use regular expression to find the numbers following the string
matches = re.findall(r'L1Dcache\.m_demand_misses\s+(\d+)', data)


# # Extracted numbers
numbers = [int(match) for match in matches]


print(sum(numbers))

with open('FYP_Extractor\MESI-16.txt', 'r') as file:
    data = file.read()

# # Use regular expression to find the numbers following the string
matches = re.findall(r'L1Dcache\.m_demand_misses\s+(\d+)', data)


# # Extracted numbers
numbers = [int(match) for match in matches]


print(sum(numbers))

with open('FYP_Extractor\MESI-64.txt', 'r') as file:
    data = file.read()

# # Use regular expression to find the numbers following the string
matches = re.findall(r'L1Dcache\.m_demand_misses\s+(\d+)', data)


# # Extracted numbers
numbers = [int(match) for match in matches]


print(sum(numbers))