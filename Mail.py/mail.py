'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 이메일 주소와 이름을 매핑하는 딕셔너리
email_dict = {
    "홍길동": "honggildong@example.com",
    "김철수": "kimcheolsu@example.com",
    "이영희": "leeyounghee@example.com"
}

def send_email(to_email, subject, body):
    # Gmail SMTP 서버 설정
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "your_email@gmail.com"  # 발신자 이메일 주소
    password = "your_app_password"  # 앱 비밀번호

    # 이메일 메시지 생성
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # SMTP 서버에 연결하고 로그인
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)

        # 이메일 전송
        server.sendmail(from_email, to_email, msg.as_string())
        print(f"이메일이 {to_email} 주소로 성공적으로 전송되었습니다.")
    except Exception as e:
        print(f"이메일 전송 중 오류가 발생했습니다: {e}")
    finally:
        server.quit()

def main():
    name = input("이름을 입력하세요: ")
    if name in email_dict:
        to_email = email_dict[name]
        subject = "테스트 이메일"
        body = "이것은 테스트 이메일입니다."
        send_email(to_email, subject, body)
    else:
        print("해당 이름에 대한 이메일 주소를 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
'''
