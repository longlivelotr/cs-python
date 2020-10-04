username=input("请输入您的姓名:")
password=input("请输入您的密码:")
if username=="admin":
    if password=="123456":
        print("输入正确，恭喜进入！")
    else:
        print("密码有误，请重试！")
else:
    print("用户名有误，请重试！")
