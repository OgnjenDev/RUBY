// sound.c - Ruby OS Audio Driver

#include <stdio.h>
#include <stdint.h>

void sound_init() {
    printf("[SOUND] Initializing PCM audio codec...\n");
}

void sound_play_tone(uint16_t frequency, uint16_t duration_ms) {
    printf("[SOUND] Playing tone: %d Hz for %d ms\n", frequency, duration_ms);
}