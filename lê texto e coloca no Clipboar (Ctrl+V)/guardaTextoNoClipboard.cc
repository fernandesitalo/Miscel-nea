#include <bits/stdc++.h>
#include <Windows.h>
using namespace std;

int main(){
	string s,out;
	freopen("entrada_____________________","r",stdin);
	while(cin >> s) out += s,out += ' ';
	
	
	// coloca string out no clipboard do teclado, usa a biblioteca <Windows.h>
	HGLOBAL hMem =  GlobalAlloc(GMEM_MOVEABLE, out.size()+ 1);
	memcpy(GlobalLock(hMem), out.data(), out.size() + 1);
	GlobalUnlock(hMem);
	OpenClipboard(0);
	EmptyClipboard();
	SetClipboardData(CF_TEXT, hMem);
	CloseClipboard();
	return 0;
}
