import config, console
from arduino import lcd
import argparse
 


def _args():
    parser = argparse.ArgumentParser()
    parser.add_argument('display', nargs='?', const='cmd')
    return parser.parse_args()


def main():
    args = _args()
    display = 'cmd'
    if args.display:
        display = (args.display).lower()
    if display in ('lcd'):
        cfg = config.get_settings('arduino_lcd')
        lcd.load(cfg)
    elif display in ('console', 'command', 'cmd'):
        cfg = config.get_settings('console')
        console.load(cfg)




if __name__ == '__main__':
    main()