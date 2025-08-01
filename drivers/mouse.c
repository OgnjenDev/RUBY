// mouse.c - Ruby OS Mouse Driver

#include <stdio.h>
#include <stdint.h>

static int cursor_x = 512;
static int cursor_y = 384;

void mouse_init() {
    printf("[MOUSE] Initializing USB mouse driver...\n");
}

void mouse_packet_received(int dx, int dy, uint8_t buttons) {
    cursor_x += dx;
    cursor_y += dy;

    printf("[MOUSE] Moved to (%d, %d), buttons: 0x%02X\n", cursor_x, cursor_y, buttons);
}