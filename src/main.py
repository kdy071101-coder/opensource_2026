
# SSH 로그인 실패 탐지 프로그램

failed_logins = [
    "192.168.0.1",
    "192.168.0.1",
    "192.168.0.2",
    "192.168.0.1",
    "192.168.0.1",
    "192.168.0.1"
]

threshold = 5
print("SSH 로그인 실패 탐지 프로그램 시작")
print(f"탐지 기준: {threshold}회 이상")

for ip in set(failed_logins):
    count = failed_logins.count(ip)

    if count >= threshold:
        print(f"[경고] {ip}: 로그인 실패 {count}회")
    else:
        print(f"[정상] {ip}: 로그인 실패 {count}회")

print("\n로그인 실패 탐지 완료")
print(f"총 로그인 실패 횟수: {len(failed_logins)}회")
