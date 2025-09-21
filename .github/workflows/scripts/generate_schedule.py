import json, datetime, requests, os

# 读成员列表
with open('members.json') as f:
    members = json.load(f)

# 读当前事件（保留已 done 的 URL）
schedule_file = 'docs/data/schedule.json'
events = []
if os.path.exists(schedule_file):
    with open(schedule_file) as f:
        events = json.load(f)

# 计算未来 7 天 （包括今天）
today = datetime.date.today()
days = [today + datetime.timedelta(days=i) for i in range(7)]

# 轮流排班
for i, d in enumerate(days):
    member = members[i % len(members)]

    # 默认 pending
    events.append({
        'date': d.isoformat(),
        'title': member,
        'desc': '',
        'status': 'pending',
        'url': ''
    })

# 写出 JSON
os.makedirs('docs/data', exist_ok=True)
with open(schedule_file, 'w', encoding='utf-8') as f:
    json.dump(events, f, ensure_ascii=False, indent=2)