import socket
import ipaddress
from openpyxl import Workbook

# Функция для получения имени хоста по IP адресу
def get_host(ip):
    try:
        host = socket.gethostbyaddr(ip)
        return host[0]
    except socket.herror:
        return "Unknown"

# Создаем новую книгу Excel
wb = Workbook()
ws = wb.active
ws.append(["IP Address", "Host Name"])

# Получаем локальный IP адрес и маску подсети
local_ip = socket.gethostbyname(socket.gethostname())
subnet = ipaddress.ip_network(local_ip + "/24", strict=False)

# Сканируем диапазон IP адресов и сохраняем результаты в Excel
for ip in subnet.hosts():
    ip_str = str(ip)
    host = get_host(ip_str)
    ws.append([ip_str, host])

# Сохраняем результаты в файл
wb.save("Scan_results.xlsx")
wb.close()