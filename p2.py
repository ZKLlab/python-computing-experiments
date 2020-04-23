from datetime import datetime, timedelta

if __name__ == '__main__':

    while True:
        try:
            time_raw = input('请输入时间(HH:MM:SS): ')
            time = datetime.strptime(time_raw, '%H:%M:%S')
            time += timedelta(seconds=1)
            print(time.strftime('%H:%M:%S'))
        except ValueError:
            print('格式有误或时间不存在！')

# 测试用例参考：
# 23:59:59
# 24:02:23
