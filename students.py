input_file = input("Zadej název vstupního souboru: ")
output_file = input_file.replace('.txt', '.sql')

with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
        name = line.strip()
        table_name = name.lower().replace(' ', '_')
        f_out.write(f"CREATE DATABASE {table_name} CHARACTER SET utf8 COLLATE utf8_czech_ci;\n")
        f_out.write(f"CREATE USER '{table_name}'@'localhost' IDENTIFIED BY '{table_name}123.';\n")
        f_out.write(f"GRANT ALL PRIVILEGES ON {table_name}.* TO '{table_name}'@'localhost' WITH GRANT OPTION;\n")
        
print(f"Soubor {output_file} byl vytvořen.")




        

