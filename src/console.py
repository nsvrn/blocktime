import time
from rich.live import Live
from rich.table import Table
from fetch_data.btc_stats import get_btc_stats
import numpy as np
from datetime import datetime as dtm


def _table(stats, colors):
    if stats: 
        tbl = Table(show_header=False, show_lines=True, border_style='white')
        datestr = dtm.now().strftime('%a %b %-d')
        timestr = dtm.now().strftime('%-I:%M %p')        
        vlist = []
        vlist.append([':calendar:', datestr, ':hourglass:', timestr])
        vlist.append([':orange_square:', f"{stats['height']}", ':watch:', f"{stats['mtime']}"])
        vlist.append([':money_bag:', f"{stats['price']}", ':money_with_wings:', f"{stats['fee']}"])
        vlist.append([':zap:', f"{stats['hrate']}", ':game_die:', stats['diff']])
        vlist.append([':robot:', stats['nodes'], ':orange_heart:', '₿locktime'])
        alternate = False
        for v in vlist: 
            alternate = not alternate
            clr = colors[0+int(alternate)]
            v3 = f'[{clr}]{v[1]}'
            if 'nodes' in v[0]: v3 = '[#f2a900]  :heart:'
            tbl.add_row(v[0], f'[{clr}]{v[1]}', v[2], f'[{clr}]{v[3]}')
        return tbl


def load(cfg):
    stats = None
    ff = int(cfg['fetch_freq']) * 60
    colors = cfg['font_colors']
    with Live(_table(stats, colors), refresh_per_second=1) as live:
        while(True):
            for i in range(0, ff):
                if i == 0: 
                    stats = get_btc_stats()
                    is_updated = True
                else:
                    is_updated = False
                live.update(_table(stats, colors))
                time.sleep(1)

