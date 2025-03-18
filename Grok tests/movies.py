def extract_movies(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for i in range(0, len(lines), 5):
        title = lines[i].strip()
        year = lines[i + 2].strip().split(': ')[1]
        print(title)
        print(year)
        print()

if __name__ == "__main__":
    extract_movies('movies.txt')