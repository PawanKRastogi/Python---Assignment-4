File_Text = input('Enter Text to write to the file: ')
with open('output.txt','w') as file1:
    file1.write(File_Text)
    print('data successfully written to ', file1.name,'.')
Append_text = input('Input additional data to append: ')
with open('output.txt','a') as file1:
    file1.write('\n'+  Append_text)
    print('Data successfully appended')

