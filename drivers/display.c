// display.c - Ruby OS VGA Display Driver

#include <stdio.h>
#include <stdint.h>

#define DISPLAY_WIDTH 1024
#define DISPLAY_HEIGHT 768

void display_init() {
    printf("[DISPLAY] VGA display initialized at %dx%d\n", DISPLAY_WIDTH, DISPLAY_HEIGHT);
}

void display_draw_pixel(uint16_t x, uint16_t y, uint32_t color) {
    if (x >= DISPLAY_WIDTH || y >= DISPLAY_HEIGHT) return;
    printf("[DISPLAY] Pixel (%d, %d) = 0x%X\n", x, y, color);
}