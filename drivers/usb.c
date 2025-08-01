// usb.c - Ruby OS USB Host Controller Driver

#include <stdio.h>
#include <stdint.h>
#include <string.h>

typedef struct {
    uint16_t vendor_id;
    uint16_t product_id;
    char manufacturer[32];
    char product[32];
} usb_device_t;

#define MAX_USB_DEVICES 8
static usb_device_t connected_devices[MAX_USB_DEVICES];
static uint8_t device_count = 0;

void usb_init() {
    printf("[USB] Initializing USB Host Controller Interface (xHCI)...\n");
    device_count = 0;
    // In real OS: setup I/O ports, memory mapping, IRQ handlers
}

void usb_add_device(uint16_t vendor, uint16_t product, const char* mfr, const char* name) {
    if (device_count >= MAX_USB_DEVICES) {
        printf("[USB] Maximum device limit reached.\n");
        return;
    }

    usb_device_t* dev = &connected_devices[device_count++];
    dev->vendor_id = vendor;
    dev->product_id = product;
    strncpy(dev->manufacturer, mfr, sizeof(dev->manufacturer));
    strncpy(dev->product, name, sizeof(dev->product));

    printf("[USB] Device connected: %s %s (VID:0x%04X PID:0x%04X)\n",
           dev->manufacturer, dev->product, dev->vendor_id, dev->product_id);
}

void usb_list_devices() {
    printf("[USB] Connected USB Devices (%d):\n", device_count);
    for (uint8_t i = 0; i < device_count; ++i) {
        usb_device_t* dev = &connected_devices[i];
        printf("  %d. %s %s (VID:0x%04X PID:0x%04X)\n",
               i + 1, dev->manufacturer, dev->product, dev->vendor_id, dev->product_id);
    }
}