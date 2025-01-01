from path.to.your.file import filter_by_response_time, filter_by_success_rate, filter_by_location, remove_duplicates, remove_charity_proxies, generate_clash_config

# 示例用法
proxies = [
    {'name': '节点1', 'ip': '192.168.1.1', 'port': 8080, 'response_time': 0.5, 'success_rate': 95, 'country': 'JP'},
    {'name': '节点2', 'ip': '192.168.1.2', 'port': 8080, 'response_time': 1.2, 'success_rate': 80, 'country': 'HK'},
    {'name': '节点3', 'ip': '192.168.1.3', 'port': 8080, 'response_time': 0.8, 'success_rate': 90, 'country': 'MO'},
    {'name': '公益节点4', 'ip': '192.168.1.4', 'port': 8080, 'response_time': 0.7, 'success_rate': 85, 'country': 'KR'},
    {'name': '节点5', 'ip': '192.168.1.1', 'port': 8080, 'response_time': 0.5, 'success_rate': 95, 'country': 'SG'},
]

# 筛选出响应时间小于 1 秒的代理节点
filtered_proxies = filter_by_response_time(proxies, 1)

# 筛选出成功率大于 90% 的代理节点
filtered_proxies = filter_by_success_rate(filtered_proxies, 90)

# 筛选出位于指定国家/地区的代理节点
allowed_countries = ['JP', 'HK', 'MO', 'KR', 'SG']
filtered_proxies = filter_by_location(filtered_proxies, allowed_countries)

# 去除重复节点
filtered_proxies = remove_duplicates(filtered_proxies)

# 去除名称带有“公益”字样的节点
filtered_proxies = remove_charity_proxies(filtered_proxies)

# 生成Clash客户端的订阅配置
clash_config = generate_clash_config(filtered_proxies)
print(clash_config)
