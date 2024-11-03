import socket  # تم تصحيح اسم المكتبة من soket إلى socket
import requests

def get_ip_info(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'fail':
            print(f"فشل في الحصول على معلومات عن IP: {ip}")
            return

        print(f"عنوان IP: {data['query']}")
        print(f"المدينة: {data['city']}")
        print(f"الولاية: {data['regionName']}")
        print(f"البلد: {data['country']}")
        print(f"مزود الخدمة: {data['isp']}")
        print(f"التوقيت: {data['timezone']}")
        
    except Exception as e:
        print(f"حدث خطأ: {e}")

# استدعاء الدالة مع عنوان IP
get_ip_info('8.8.8.8')  # يمكنك تغيير هذا إلى أي عنوان IP تريده