// battery.c - Ruby OS Battery Monitor Driver

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void battery_init() {
    srand(time(NULL));
    printf("[BATTERY] Battery monitor active\n");
}

void battery_check_status() {
    int level = rand() % 100;
    int charging = rand() % 2;

    printf("[BATTERY] Level: %d%% | Charging: %s\n", level, charging ? "YES" : "NO");
}