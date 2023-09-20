
from collections import defaultdict

total_entries = 0
unique_ips = set()
http_requests = defaultdict(int)
ip_count = defaultdict(int)

with open('access.log', 'r') as log_file:
  for line in log_file:
    total_entries += 1
    parts = line.split()
    
    ip_address = parts[0]
    http_request = parts[7]
    
    unique_ips.add(ip_address)
    http_requests[http_request] += 1
    ip_count[ip_address] += 1
    
# Print the results
print("Total number of access entries:", total_entries)

print("Unique IP addresses:")
for ip in unique_ips:
    print(ip)
    
print("HTTP requests and their counts:")
for request, count in http_requests.items():
    print(f"{request}: {count} times")
    
print("Top 5 most frequent IP addresses:")
sorted_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:5]
for ip, count in sorted_ips:
    print(f"{ip}: {count} times")