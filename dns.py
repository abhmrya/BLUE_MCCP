from ipaddress import ip_address, ip_network

routes = [
    ("10.0.0.0/8", "Transit Gateway"),
    ("10.20.0.0/16", "VPC Peering"),
    ("10.20.1.0/24", "Specific route"),
    ("0.0.0.0/0", "Internet Gateway"),
]

destination = ip_address("10.20.1.114")

matching_routes = [
    (ip_network(cidr), target)
    for cidr, target in routes
    if destination in ip_network(cidr)
]

best_route = max(
    matching_routes,
    key=lambda route: route[0].prefixlen,
)

print(f"Destination: {destination}")
print(f"Selected route: {best_route[0]}")
print(f"Selected target: {best_route[1]}")