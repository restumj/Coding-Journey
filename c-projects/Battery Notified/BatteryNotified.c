#include <stdio.h>
#include <windows.h>
#include <stdbool.h>

int main() {
    SYSTEM_POWER_STATUS status;

    bool notified = false, notifiedFullCharge = false;
    
    while (true) {
        if (GetSystemPowerStatus(&status)) {
            int level = status.BatteryLifePercent;
            bool charging = (status.ACLineStatus == 1);

            if (charging && level == 100 && !notifiedFullCharge) {
                MessageBox(NULL,TEXT("Baterai sudah penuh!"),TEXT("Notifikasi Baterai"),MB_OK|MB_ICONINFORMATION);
                notifiedFullCharge = true;
            }

            if (!charging && level == 98 && !notified) {
                MessageBox(NULL,TEXT("Baterai sudah 98%."),TEXT("Notifikasi Baterai"),MB_OK|MB_ICONWARNING);
                notified = true;
                break;
            }
        } else {
            MessageBox(NULL,TEXT("Gagal membaca status baterai."),TEXT("Error"),MB_OK|MB_ICONWARNING);
        }
        Sleep(60000);
    }
    return 0;
}