import json

def filter_by_response_time(proxies, max_response_time):
    """
    筛选出响应时间小于 max_response_time 的代理节点
    :param proxies: 代理节点列表，每个节点是一个字典，包含 'response_time' 键
    :param max_response_time: 最大响应时间（秒）
    :return: 筛选后的代理节点列表
    """
    return [proxy for proxy in proxies if proxy['response_time'] <= max_response_time]

def filter_by_success_rate(proxies, min_success_rate):
    """
    筛选出成功率大于 min_success_rate 的代理节点
    :param proxies: 代理节点列表，每个节点是一个字典，包含 'success_rate' 键
    :param min_success_rate: 最小成功率（百分比）
    :return: 筛选后的代理节点列表
    """
    return [proxy for proxy in proxies if proxy['success_rate'] >= min_success_rate]

def filter_by_location(proxies, allowed_countries):
    """
    筛选出位于 allowed_countries 列表中的代理节点
    :param proxies: 代理节点列表，每个节点是一个字典，包含 'country' 键
    :param allowed_countries: 允许的国家列表
    :return: 筛选后的代理节点列表
    """
    return [proxy for proxy in proxies if proxy['country'] in allowed_countries]

def remove_duplicates(proxies):
    """
    去除重复的代理节点
    :param proxies: 代理节点列表
    :return: 去重后的代理节点列表
    """
    seen = set()
    unique_proxies = []
    for proxy in proxies:
        identifier = (proxy['ip'], proxy['port'])
        if identifier not in seen:
            seen.add(identifier)
            unique_proxies.append(proxy)
    return unique_proxies

def remove_charity_proxies(proxies):
    """
    去除名称带有“公益”字样的代理节点
    :param proxies: 代理节点列表
    :return: 过滤后的代理节点列表
    """
    return [proxy for proxy in proxies if '公益' not in proxy['name']]

def generate_clash_config(proxies):
    """
    生成Clash客户端的订阅配置
    :param proxies: 代理节点列表
    :return: Clash配置的JSON字符串
    """
    clash_proxies = []
    for proxy in proxies:
        clash_proxies.append({
            'name': proxy['name'],
            'type': 'http',
            'server': proxy['ip'],
            'port': proxy['port'],
            'username': proxy.get('username', ''),
            'password': proxy.get('password', '')
        })
    config = {
        'proxies': clash_proxies,
        'proxy-groups': [],
        'rules': []
    }
    return json.dumps(config, indent=2)
