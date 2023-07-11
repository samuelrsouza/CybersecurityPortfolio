import  time
import  psutil

last_recieved = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_sent + last_recieved

while True:
    bytes_recieved = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_recieved + bytes_sent

    band_recieved = bytes_recieved - last_recieved
    band_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total

    mb_new_recieved = band_recieved / 1024 / 1024
    mb_new_sent = band_sent / 1024 / 1024
    mb_new_total = new_total / 1024 / 1024


    print(f"{mb_new_recieved:.2f} MB recieved, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total")

    last_recieved = bytes_recieved
    last_sent = bytes_sent
    last_total = bytes_total

    time.sleep(1)