from collections import Counter


def get_count_visits_from_ip(ips):
    freak_ip = Counter(ips)
    return freak_ip

def get_frequent_visit_from_ip(ips):
    freak_ip = Counter(ips)
    freak = freak_ip.most_common(1)[0]
    return freak