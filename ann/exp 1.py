def load_dataset(file_path): 
    dataset = [] 
 
    with open(file_path, 'r') as file:         
        for line in file: 
            values = line.strip().split(',')             
            dataset.append(values) 
 
    return dataset 
 
def print_tabular(dataset): 
    column_widths = [max(len(str(item)) for item in column) for column in zip(*dataset)] 
  
    headers = dataset[0] 
    header_line = ' | '.join(f'{header:^{width}}' for header, width in zip(headers, column_widths))     
    print(header_line)     
    print('-' * (sum(column_widths) + len(column_widths) * 3 - 1)) 
 
    for row in dataset[1:]: 
        row_line = ' | '.join(f'{value:<{width}}' for value, width in zip(row, column_widths)) 
        print(row_line) 
 
file_path = 'data.csv' 
loaded_dataset = load_dataset(file_path) 
print_tabular(loaded_dataset) 
