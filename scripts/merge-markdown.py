import os

def merge_markdown_files(directory):
    # Initialize a counter for numbering
    counter = 1
    # Output file to store the merged content
    output_filename = f"{directory}.md"
    
    # Open the output file in write mode
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        # Iterate through all files in the specified directory
        for filename in sorted(os.listdir(directory)):
            # Check if the file is a Markdown file
            if filename.endswith('.md'):
                # Generate the delimiter with the file title and incrementing number
                delimiter = f'\n\n# Tweet Number {counter}: {os.path.splitext(filename)[0]}\n\n'
                # Increment the counter for the next file
                counter += 1
                
                # Write the delimiter to the output file
                output_file.write(delimiter)
                
                # Open and read the current markdown file
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    # Write the content of the markdown file to the output file
                    output_file.write(file.read())

    print(f"All markdown files have been merged into {output_filename}")

# Specify the directory containing markdown files
directory_path = r'C:\Private\Repositories\content-creation\threads'
merge_markdown_files(directory_path)
