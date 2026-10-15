while True:
    filename = input("읽을 파일명을 입력하세요 (종료는 q): ")
    if filename.lower() == 'q':
        break

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for i, line in enumerate(lines, 1):
            print(f"{i} {line}", end='')

        base_name = filename.rsplit('.', 1)[0] if '.' in filename else filename
        sav_filename = f"{base_name}.sav"

        with open(sav_filename, 'w', encoding='utf-8') as f_out:
            for i, line in enumerate(lines, 1):
                f_out.write(f"{i} {line}")

        print(f"\n'{sav_filename}' 파일로 저장되었습니다.")
        break

    except FileNotFoundError:
        print("파일이 존재하지 않습니다. 다시 입력해주세요.")