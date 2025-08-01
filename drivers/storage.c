// storage.c - Ruby OS SATA Storage Driver

#include <stdio.h>
#include <stdint.h>

void storage_init() {
    printf("[STORAGE] SATA interface initialized (AHCI mode)\n");
}

void storage_read_block(uint32_t lba) {
    printf("[STORAGE] Reading LBA block %u\n", lba);
}

void storage_write_block(uint32_t lba) {
    printf("[STORAGE] Writing LBA block %u\n", lba);
}