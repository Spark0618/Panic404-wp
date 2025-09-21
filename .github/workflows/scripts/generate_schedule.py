import json, datetime, requests, os

# 读成员列表
with open('members.json') as f:
    members = json.load(f)

# 读当前事件（保留已 done 的 URL）
schedule_file = '././docs/data/schedule.json'
old = []
if os.path.exists(schedule_file):
    with open(schedule_file) as f:
        old = json.load(f)

# 计算未来 6 天
today = datetime.date.today()
days = [today + datetime.timedelta(days=i) for i in range(6)]

# 轮流排班
events = []
for i, d in enumerate(days):
    member = members[i % len(members)]
    # 默认 pending
    status = 'pending'
    url = ''

    # 如果 old 里当天该成员有 done，则保留 done 和 url
    for ev in old:
        if ev['date'] == d.isoformat() and ev['title'] == member and ev['status'] == 'done':
            status = 'done'
            url = ev['url']
            break

    events.append({
        'date': d.isoformat(),
        'title': member,
        'type': '',
        'status': status,
        'url': url
    })

# 5. 检查 GitHub 是否有该成员提交（简单示例）
# 这里可以调用 GitHub API 查询最近 push，如果找到就 status='done' url='...'
# 示例：requests.get(f'https://api.github.com/repos/<org>/<repo>/commits?author={member}')

# 6. 写出 JSON
os.makedirs('data', exist_ok=True)
with open(schedule_file, 'w', encoding='utf-8') as f:
    json.dump(events, f, ensure_ascii=False, indent=2)