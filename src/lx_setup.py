import sys, time
import serial
import lewansoul_lx16a

#SERIAL_PORT = '/dev/ttyUSB0'    # For Linux
SERIAL_PORT = 'COM3'            # For Windows (find port in Device Manager -> Ports)

ctrl = lewansoul_lx16a.ServoController(
    serial.Serial(SERIAL_PORT, 115200, timeout=1),
)

def servo_info(id):
    print("Servo id: {}".format(id))
    print("Position: {}".format(ctrl.get_position(id)))
    print("Temperature: {}".format(ctrl.get_temperature(id)))

if __name__ == '__main__':
    args = sys.argv[1:]
    args_num = len(args)
    if args_num == 0:
        try:
            id = ctrl.get_servo_id()
            if id != 255:
                servo_info(id)
        except:
            print('Error!')
    elif args[0] == 'info':
        servo_info(int(args[1]))
    elif args[0] == 'assign' and args_num == 3:
        ctrl.set_servo_id(int(args[1]), int(args[2]))
    elif args[0] == 'test' and args_num == 2:
        id = int(args[1])
        ctrl.move(id, 0, 500)
        time.sleep(1)
        ctrl.move(id, 1000, 500)
        time.sleep(1)
        ctrl.move(id, 500, 500)
    elif args[0] == 'set_pos' and args_num == 3:
        ctrl.move(int(args[1]), int(args[2]), 500)
    elif args[0] == 'reset' and args_num == 2:
        id = int(args[1])
        ctrl.set_servo_id(id, 1)
        ctrl.set_position_offset(id, 0)
        ctrl.save_position_offset(id)
    elif args[0] == 'scan':
        print("Found servo ids:")
        for i in range(1, 255):
            try:
                ctrl.get_position(i, 0.01)
                print(i)
            except:
                pass
    else:
        print("\
Usage:\n\
python lx_setup.py info 1\n\
python lx_setup.py assign 1 10\n\
python lx_setup.py test 1\n\
python lx_setup.py set_pos 1 500\n\
python lx_setup.py reset 1\n\
python lx_setup.py scan\n")
