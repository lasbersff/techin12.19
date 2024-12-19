def convert_to_cm(file_path):
    conversion_rates = {
        'ft': 30.48,
        'in': 2.54,
        'mil': 160934,
        'yd': 91.44,
        'wm': 60
    }
    total_cm = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip() 
        for unit in conversion_rates:
            if line.endswith(unit):
                try:
                    value = float(line[:-len(unit)])  
                    total_cm += value * conversion_rates[unit]
                except ValueError:
                    print(f"Invalid: {line}")
                break

    return round(total_cm, 2)

data_file = 'names.txt'
result = convert_to_cm(data_file)
print(f"Total: {result}cm")
