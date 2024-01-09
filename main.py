
import json
import os
from pprint import pprint

from vkapi import VkApi
from yadiskapi import YaDiskApi

CONFIG_FILENAME = 'config.txt'

if __name__ == '__main__':
    vk_token = None
    ya_disk_token = None

    # load VK token and Yandex.Disk token from config file
    if os.path.exists(CONFIG_FILENAME):
        try:
            with open(CONFIG_FILENAME, 'rt') as config_file:
                config = json.load(config_file)
                vk_token = config['vk token']
                try:
                    ya_disk_token = config['yandex disk token']
                except:
                    # Yandex.Disk token will be asked to input by user
                    pass
        except Exception as config_err:
            print(f'Error while reading config file:\n{type(config_err)}\n{config_err}')
    else:
        print('Config file not found. See "config_example.txt"')
    
    if vk_token is None:
        print('Load VK token from config file failed.')
        vk_token = input('Please, input VK token value: ')
        if not vk_token:
            print('VK token is necessary to run the program!')
            exit()
    
    try:
        vk_user_id = int(input("Please, input VK user ID to upload profile's photos: "))
    except:
        print('VK user ID should be valid integer value!')
        exit()

    # print('Load Yandex.Disk token from config file failed.')
    ya_disk_token_input = input('Please, input Yandex.Disk token value (leave it empty to read it from config.txt): ')
    if ya_disk_token_input:
        ya_disk_token = ya_disk_token_input
    if not ya_disk_token:
        print('Yandex.Disk token is necessary to run the program! It should be input by user or load from config file.')
        exit()

    # print(f'VK token: {vk_token}')
    # print(f'Yandex.Disk token: {ya_disk_token}')

    user_vk_api = VkApi(vk_token)
    user_ya_disk_api = YaDiskApi(ya_disk_token)

    vk_album_id = str(input('Please, input album ID (profile by default): ') or 'profile')
    photos_cnt = int(input('Please, input photos number to be uploaded (5 by default): ') or 5)

    user_vk_api.save_photos_to_yadisk(user_id=vk_user_id, ya_disk_api=user_ya_disk_api, album=vk_album_id, count=photos_cnt)
