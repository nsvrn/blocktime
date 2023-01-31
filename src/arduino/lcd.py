import serial, time
from fetch_data.btc_stats import get_btc_stats



def print_to_lcd(p: serial.Serial, fetch_freq, page_delay):
  if p.isOpen():
    while (True):
      stats = get_btc_stats()
      page_delay = int(page_delay)
      repeat_times = int( (int(fetch_freq)*60)/(page_delay*len(stats)) )
      for _ in range(0, repeat_times):
        for k, v in stats.items():
          p.write(f'{v}'.encode())
          time.sleep(page_delay)
      


def load(cfg):
  port = serial.Serial(cfg['device'], cfg['baudrate'])
  time.sleep(2)
  print_to_lcd(port, cfg['fetch_freq'], cfg['page_delay'])