// power.c - Ruby OS Advanced Power Management Driver

#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

// Simulacija ACPI statusa
static bool system_awake = true;
static uint8_t power_state = 0; // 0 = S0 (on), 5 = S5 (soft off)

void power_init() {
    printf("[POWER] ACPI interface initialized.\n");
    printf("[POWER] Current power state: S0 (Working)\n");
}

void power_enter_sleep() {
    if (!system_awake) {
        printf("[POWER] System already in sleep mode.\n");
        return;
    }

    printf("[POWER] Entering S3 (Suspend to RAM)...\n");
    power_state = 3;
    system_awake = false;
}

void power_wake() {
    if (system_awake) {
        printf("[POWER] System already awake.\n");
        return;
    }

    printf("[POWER] Waking from S3 (Resume)...\n");
    power_state = 0;
    system_awake = true;
}

void power_shutdown() {
    printf("[POWER] Executing S5 shutdown...\n");
    power_state = 5;
    system_awake = false;
}

void power_reboot() {
    printf("[POWER] Soft reboot triggered via ACPI reset...\n");
    power_state = 0;
    system_awake = true;
}