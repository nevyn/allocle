import display
import device
import time
import gc
import uasyncio
import led

def gui_bar(percentage, x, width = 75):
    frame = display.Polyline([x, 0, x+width, 0, x+width, 24, x, 24, x, 0], display.WHITE, thickness=1)
    bar = display.Line(x + 5, 12, x + 5 + int(percentage * width), 12, display.GREEN, thickness=12)
    return [frame, bar]

def widget_battery():
    battery_level = (device.battery_level() / 100)
    time_remaining_label = display.Text(f'{int(battery_level * 67)}m', 565, 50, display.WHITE, justify=display.MIDDLE_LEFT)
    return gui_bar(battery_level, 565) + [time_remaining_label]

def widget_mem():
    mem_free = gc.mem_free()
    mem_level = gc.mem_alloc() / (gc.mem_alloc() + mem_free)
    mem_free_label = display.Text(f'{int(mem_free * 67)}b', 460, 50, display.WHITE, justify=display.MIDDLE_LEFT)
    return gui_bar(mem_level, 460)

def widget_time():
    now = time.now()
    nowlabel = "{:0>2}:{:0>2}:{:0>2}".format(now["hour"], now["minute"], now["second"])
    return display.Text(nowlabel, 0, 0, display.WHITE, justify=display.TOP_LEFT)

def draw_frame():
    display.show([
        widget_time(),
        widget_mem(),
        widget_battery()
    ])

async def a_display_loop():
    while True:
        draw_frame()
        gc.collect()
        await uasyncio.sleep_ms(1000)

async def a_blink(color, period_ms):
    while True:
        led.on(color)
        await uasyncio.sleep_ms(period_ms)
        led.off(color)
        await uasyncio.sleep_ms(period_ms)

async def main():
    draw_frame()
    await uasyncio.gather(
        uasyncio.create_task(a_blink(led.RED, 100)),
        uasyncio.create_task(a_display_loop())
    )
    

uasyncio.run(main())
