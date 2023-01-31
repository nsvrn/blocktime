#### ₿locktime

---
##### Setup
- For setting up arduino and LCD display:
    - Verify the script `src/arduino/lcd.ino`(taken from arduino IDE Examples > SerialDisplay) and upload to your arduino
    - For the hardware setup, follow this [video](https://www.youtube.com/watch?v=_6_F6B0rd6M)
    - Make sure your data pins match the numbers in the `lcd.ino` script(not the video)
- Install dependencies: `pip install -r requirements.txt`
- Setup `settings.conf` (copy from `settings.sample.conf` as same folder location)
- After you connect via USB you will have to set the read/write permissions(use name of your serial device instead of `/dev/ttyACM0`):
```
    chmod a+rw /dev/ttyACM0
```


---
##### Run


- The data updates every x minutes as setup in the `settings.conf`
```
    cd src &&
    python3 blocktime console
```
![alt blocktime_console](blocktime_console.png)


```
    python3 blocktime lcd
```
<video src="https://user-images.githubusercontent.com/120062368/215665950-1288a0fc-420f-4e0b-b3a7-4f6c2da62705.mp4">

