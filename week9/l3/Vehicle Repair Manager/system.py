from baseUser import create_BaseUser_table
from client import create_Client_table
from mechanic import create_Mechanic_table
from vehicle import create_Vehicle_table, add_vehicle, list_all_vehicles, update_vehicle, delete_vehicle
from service import create_Service_table, add_service, list_all_services
from vehicle_repair import create_vehicle_repair, add_vehicle_repair
from mechanic_service import create_mechanic_service, add_mechanic_service
from hours import (create_hours_table,
                   list_all_free_hours,
                   list_all_busy_hours,
                   list_free_hours,
                   list_busy_hours,
                   add_hour,
                   update_repair_hour,
                   update_repair_hour_for_clients,
                   delete_repair_hour
                   )
from utls import (check_if_user_is_in_the_system,
                  create_user_if_not_in_the_system,
                  get_user_type,
                  display_menu_for_client,
                  display_menu_for_mechanic,
                  get_mechanic_id,
                  get_service_id,
                  get_username,
                  get_id_from_username
                  )


def create_all_tables():
    create_BaseUser_table()
    create_Client_table()
    create_Mechanic_table()
    create_Vehicle_table()
    create_Service_table()
    create_vehicle_repair()
    create_mechanic_service()
    create_hours_table()


def main():
    create_all_tables()
    print('Hello!')
    username = input('Provide username: ')
    if check_if_user_is_in_the_system(username) is False:
        print('Unknown user!')
        if create_user_if_not_in_the_system() is False:
            return
        user_type = get_user_type()
        username = get_username()
        print(f'''
Thank you, {username}!
Welcome to Vehicle Services!
Next time you try to login, provide your user_name!
''')
    else:
        print(f'Hello, {username}')
        user_type = get_user_type(username)
    if user_type == 'Mechanic':
        display_menu_for_mechanic()
        choice = input()
        choice = choice.split(' ')
        while choice[0] != 'exit':

            if choice[0] == 'list_all_free_hours':
                list_all_free_hours()
            elif choice[0] == 'list_free_hours':
                list_free_hours(choice[1])
            elif choice[0] == 'list_all_busy_hours':
                list_all_busy_hours()
            elif choice[0] == 'list_busy_hours':
                list_busy_hours(choice[1])
            elif choice[0] == 'add_new_repair_hour':
                add_hour()
            elif choice[0] == 'add_new_service':
                add_service()
                mechanic_id = get_mechanic_id(username)
                service_id = get_service_id()
                add_mechanic_service(mechanic_id, service_id)
            elif choice[0] == 'update_repair_hour':
                update_repair_hour(int(choice[1]))
            elif choice[0] == 'exit':
                return
            display_menu_for_mechanic()
            choice = input()
            choice = choice.split(' ')
    if user_type == 'Client':
        display_menu_for_client()
        choice = str(input()).split(' ')
        while choice[0] != 'exit':
            if choice[0] == 'list_all_free_hours':
                list_all_free_hours()
            elif choice[0] == 'list_free_hours':
                list_free_hours(choice[1])
            elif choice[0] == 'save_repair_hour':
                print('Chose Vechicle to repair: ')
                user_id = get_id_from_username(username)
                list_all_vehicles(user_id)
                vehicle = input()
                print('Chose service')
                list_all_services()
                service = input()
                add_vehicle_repair(vehicle, choice[1], service)
            elif choice[0] == 'update_repair_hour':
                update_repair_hour_for_clients(choice[1])
            elif choice[0] == 'delete_repair_hour':
                delete_repair_hour(choice[1])
            elif choice[0] == 'list_personal_vehicles':
                user_id = get_id_from_username(username)
                list_all_vehicles(user_id)
            elif choice[0] == 'add_vehicle':
                user_id = get_id_from_username(username)
                add_vehicle(user_id)
            elif choice[0] == 'update_vehicle':
                update_vehicle(choice[1])
            elif choice[0] == 'delete_vehicle':
                delete_vehicle(choice[1])
            elif choice[0] == 'exit':
                return
            display_menu_for_client()
            choice = str(input()).split(' ')


if __name__ == '__main__':
    main()
