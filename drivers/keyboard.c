// keyboard.c - Ruby OS PS/2 Keyboard Driver

#include <stdio.h>
#include <stdint.h>

#define KEYBOARD_BUFFER_SIZE 256

static uint8_t keyboard_buffer[KEYBOARD_BUFFER_SIZE];
static uint8_t buffer_head = 0;
static uint8_t buffer_tail = 0;

void keyboard_init() {
    printf("[KEYBOARD] Initializing PS/2 controller...\n");
    buffer_head = 0;
    buffer_tail = 0;
}

void keyboard_interrupt_handler(uint8_t scancode) {
    uint8_t next = (buffer_head + 1) % KEYBOARD_BUFFER_SIZE;
    if (next != buffer_tail) {
        keyboard_buffer[buffer_head] = scancode;
        buffer_head = next;
    }
}

uint8_t keyboard_read_scancode() {
    if (buffer_head == buffer_tail) return 0;
    uint8_t code = keyboard_buffer[buffer_tail];
    buffer_tail = (buffer_tail + 1) % KEYBOARD_BUFFER_SIZE;
    return code;
}