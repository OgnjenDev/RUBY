// network.c - Ruby OS Network Driver

#include <stdio.h>
#include <string.h>

static char mac_address[] = "00:1A:92:FF:AB:1D";

void network_init() {
    printf("[NET] Initializing Ethernet interface (eth0)...\n");
    printf("[NET] MAC Address: %s\n", mac_address);
}

void network_send_packet(const char* data) {
    printf("[NET] TX: %s\n", data);
}

void network_receive_packet() {
    printf("[NET] RX: PING 192.168.0.1 -> 192.168.0.2\n");
}