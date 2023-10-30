import base64
import xmlrpc.client
import os

url = 'http://tuyenduong.tuoitredhqghcm.edu.vn'
db = 'main'
username = 'admin'
password = 'huy@khang@tu'

# Create Folder
list_uni = ['HCMUT', 'HCMUS', 'USSH', 'UIT',
            'UEL', 'IU', 'MED', 'ANGIANG', 'ĐHQG']
for folder_name in list_uni:
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Created folder '{folder_name}'.")
    else:
        print(f"Folder '{folder_name}' already exists.")

# Get Image
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
for user_id in range(0, 1000):  # Thay range nghen
    user_name = models.execute_kw(db, uid, password, 'res.users', 'read',
                                  [[user_id]], {'fields': ['name']})
    user_donvi = models.execute_kw(db, uid, password, 'res.users', 'read',
                                   [[user_id]], {'fields': ['donvi']})
    user_ms = models.execute_kw(db, uid, password, 'res.users', 'read',
                                [[user_id]], {'fields': ['mssv_mscb']})
    avatar_img = models.execute_kw(db, uid, password, 'res.users', 'read',
                                   [[user_id]], {'fields': ['avatar_1920']})

    if avatar_img:
        avatar_name = user_name[0]['name']  # Access the user name directly
        donvi_name = user_donvi[0]['donvi']
        if (donvi_name != False):
            donvi_name = donvi_name[1]
        ms_name = user_ms[0]['mssv_mscb']

        image_data = base64.b64decode(avatar_img[0]['avatar_1920'])
        file_name = f'{ms_name}-{avatar_name}.png'

        if donvi_name == "Đoàn Trường Đại học Bách khoa":
            with open(f'HCMUT/{file_name}', 'wb') as file:
                file.write(image_data)
        elif donvi_name == "Đoàn Trường Đại học Khoa học Tự nhiên":
            with open(f'HCMUS/{file_name}', 'wb') as file:
                file.write(image_data)
        elif donvi_name == "Đoàn Trường Đại học Khoa học Xã hội và Nhân văn":
            with open(f'USSH/{file_name}', 'wb') as file:
                file.write(image_data)
        elif donvi_name == "Đoàn Trường Đại học Công nghệ Thông tin":
            with open(f'UIT/{file_name}', 'wb') as file:
                file.write(image_data)
        elif donvi_name == "Đoàn Trường Đại học Kinh tế - Luật":
            with open(f'UEL/{file_name}', 'wb') as file:
                file.write(image_data)
        elif donvi_name == "Đoàn Trường Đại học Quốc tế":
            with open(f'IU/{file_name}', 'wb') as file:
                file.write(image_data)
        elif donvi_name == "Đoàn Trường Đại học An Giang":
            with open(f'ANGIANG/{file_name}', 'wb') as file:
                file.write(image_data)
        elif donvi_name == "Đoàn Khoa Y":
            with open(f'MED/{file_name}', 'wb') as file:
                file.write(image_data)
        elif donvi_name == "Đoàn Cơ quan ĐHQG-HCM":
            with open(f'ĐHQG/{file_name}', 'wb') as file:
                file.write(image_data)

        print(
            f'Avatar for record {avatar_img[0]["id"]} downloaded and saved as: {file_name} for {donvi_name}')
    else:
        print(f'No avatar found for record {user_id}')
