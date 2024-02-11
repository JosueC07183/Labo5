import serial
import csv
import time

def configure_serial_connection(serial_port, baud_rate):
    return serial.Serial(serial_port, baud_rate, timeout=1)

def read_serial_data(serial_connection):
    return serial_connection.readline().decode("utf-8").replace('\r', "").replace('\n', "").split(',')

def write_data_to_csv(data, csv_file):
    csv_file.writerow(data)

def main():
    serial_port = "/dev/ttyACM0"
    baud_rate = 9600
    primer_linea = ['aX', 'aY', 'aZ', 'gX', 'gY', 'gZ']
    samples = 1500
    archivo_csv = 'circle.csv'
    
    ser = configure_serial_connection(serial_port, baud_rate)
    print("NanoBLE 33 Sense conectado")

    with open(archivo_csv, 'w', newline='', encoding='UTF8') as file:
        writeFile = csv.writer(file)
        writeFile.writerow(primer_linea)

        counter = 0
        while counter < samples:
            movimiento = read_serial_data(ser)
            if len(movimiento) == 6:
                write_data_to_csv(movimiento, writeFile)
                counter += 1

if __name__ == "__main__":
    main()
