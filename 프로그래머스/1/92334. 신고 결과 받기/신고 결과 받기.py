def solution(id_list, report, k):
    # 딕셔너리로 변경
    check = {id_: [] for id_ in id_list}
    warning = {id_: 0 for id_ in id_list}
    stop = []
    mail = {id_: 0 for id_ in id_list}

    # 중복 데이터 제거
    report = list(set(report))

    # 데이터 내부 분리 및 딕셔너리에 추가
    for i in report:
        data = i.split(" ")
        sender, receiver = data[0], data[1]
        if sender in check:
            check[sender].append(receiver)
        if receiver in warning:
            warning[receiver] += 1

    # 이용 정지 당하는 사람
    for id_, count in warning.items():
        if count >= k:
            stop.append(id_)

    # 정지된 사람에게 메일 발송
    for stop_id in stop:
        for id_, receivers in check.items():
            if stop_id in receivers:
                mail[id_] += 1

    return list(mail.values())