try:
    file_1=open('Sample.txt','r')
    reading_file=file_1.read()
    print(reading_file)
    file_1.close()

except FileNotFoundError:
    print("Error: The File 'Sample.txt' not found.")