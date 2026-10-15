while True:
    filename = input("읽을 파일명을 입력하세요 (종료는 q): ")
    if filename.lower() == 'q':
        break

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        line_count = len(lines)
        word_count = 0
        char_count = 0

        for line in lines:
            words = line.split()
            word_count += len(words)
            char_count += sum(len(word) for word in words)

        print(f"characters : {char_count}")
        print(f"words      : {word_count}")
        print(f"lines      : {line_count}")
        break

    except FileNotFoundError:
        print("파일이 존재하지 않습니다. 다시 입력해주세요.")