def solution(record):
    answer = []
    key = {}

    for str in record:
        split_str = str.split(' ')
        command = split_str[0]
        u_id = split_str[1]
        if command == 'Enter' or command == 'Change':
            u_name = split_str[2]
            key[u_id] = u_name

    for str in record:
        split_str = str.split(' ')
        command = split_str[0]
        u_id = split_str[1]
        if command == 'Enter':
            answer.append(key[u_id] + '님이 들어왔습니다.')

        elif command == 'Leave':
            answer.append(key[u_id] + '님이 나갔습니다.')

    return answer

record = []
record.append("Enter uid1234 Muzi");
record.append("Enter uid4567 Prodo");
record.append("Leave uid1234");
record.append("Enter uid1234 Prodo");
record.append("Change uid4567 Ryan");

print(solution(record))
