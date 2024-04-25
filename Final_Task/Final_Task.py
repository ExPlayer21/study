import socket
import ipaddress
from openpyxl import Workbook

# Функция для получения имени хоста по IP адресу
def get_host(ip):
    try:
        host = socket.gethostbyaddr(ip)
        return host[0]
    except socket.herror:
        return "Неизвестно"

# Функция для получения маски подсети
def get_subnet_mask():
    ip = socket.gethostbyname(socket.gethostname())
    subnet_mask = sum([bin(int(x)).count('1') for x in socket.gethostbyname_ex(socket.gethostname())[2][0].split('.')])
    return f"{ip}/{subnet_mask}"

# Получаем маску подсети
subnet_mask = get_subnet_mask()

# Создаем новую книгу Excel
wb = Workbook()
ws = wb.active
ws.append(["IP адрес", "Имя ПК"])

# Получаем локальный IP адрес и добавляем маску подсети
local_ip = socket.gethostbyname(socket.gethostname())
subnet = ipaddress.ip_network(subnet_mask, strict=False)

# Сканируем диапазон IP адресов и сохраняем результаты в Excel
for ip in subnet.hosts():   
    ip_str = str(ip)
    host = get_host(ip_str)
    ws.append([ip_str, host])

# Сохраняем результаты в файл
wb.save("network_scan_results.xlsx")
wb.close()