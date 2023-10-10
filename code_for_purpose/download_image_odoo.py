import base64
import xmlrpc
import xmlrpc.client

url = 'http://localhost:8069'  # Sau thay bang url cua tuyenduong

db = 'odoo1'  # sau thay bang main
username = 'odoo'  # giu nguyen
password = 'odoo'  # giu nguyen

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Cai nay se chay tuan tu va cai user_id se bat dau bang 2
# Minh se tao mot vong
# for user_id in range (2, length user):
# ------------------------Code trong vong for-------------------------
user_id = 2  # Thay thanh user_id
# user_name = models.execute_kw(db, uid, password, 'res.users', 'read',
#                               [[user_id]], {'fields': ['name']}) # Them vao sau
avatar_img = models.execute_kw(db, uid, password, 'res.users', 'read',
                               [[user_id]], {'fields': ['avatar_128']})

if avatar_img:
    image_data = base64.b64decode(avatar_img[0]['avatar_128'])
    file_name = f'avatar_{avatar_img[0]["id"]}.png'

    with open(file_name, 'wb') as file:
        file.write(image_data)

    print(
        f'Avatar for record {avatar_img[0]["id"]} downloaded and saved as: {file_name}')
else:
    print(f'No avatar found for record {avatar_img[0]["id"]}')
