#include <Windows.h>

extern "C"
{
   static HWND hWndConsole = nullptr;
   void init_console()
   {
      hWndConsole = GetConsoleWindow();
   }

   bool has_ui_console()
   {
      return hWndConsole && ::IsWindow(hWndConsole);
   }

   bool is_ui_console_visible()
   {
      return has_ui_console() && ::IsWindowVisible(hWndConsole);
   }

   void show_ui_console(bool show)
   {
      if (has_ui_console())
      {
         if (show)
         {
            ShowWindow(hWndConsole, SW_SHOW);
            BringWindowToTop(hWndConsole);
         }
         else
            ShowWindow(hWndConsole, SW_HIDE);
      }
   }

   void clear_ui_console()
   {
      if (has_ui_console())
      {
         COORD coordScreen = { 0, 0 };
         DWORD cCharsWritten;
         CONSOLE_SCREEN_BUFFER_INFO csbi;
         DWORD dwConSize;

         HANDLE hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
         GetConsoleScreenBufferInfo(hStdOut, &csbi);
         dwConSize = csbi.dwSize.X * csbi.dwSize.Y;
         FillConsoleOutputCharacter(hStdOut, ' ', dwConSize, coordScreen, &cCharsWritten);
         GetConsoleScreenBufferInfo(hStdOut, &csbi);
         FillConsoleOutputAttribute(hStdOut, csbi.wAttributes, dwConSize, coordScreen, &cCharsWritten);
         SetConsoleCursorPosition(hStdOut, coordScreen);
      }
   }


   void stdout_stream_helper_write(const char *data)
   {
      DWORD RetVal;
      WriteFile(GetStdHandle(STD_OUTPUT_HANDLE), data, (DWORD)strlen(data), &RetVal, NULL);
   }

   void stdout_stream_helper_flush()
   {
      FlushFileBuffers(GetStdHandle(STD_OUTPUT_HANDLE));
   }

   wchar_t lpBuffer[1024];

   const wchar_t* stdin_stream_helper_readline()
   {
      if (hWndConsole && ::IsWindow(hWndConsole))
      {
         ShowWindow(hWndConsole, SW_SHOW);
         BringWindowToTop(hWndConsole);

         DWORD nRead;

         ReadConsole(GetStdHandle(STD_INPUT_HANDLE), lpBuffer, 1023, &nRead, NULL);
         lpBuffer[nRead] = '\0';
         return lpBuffer;
      }
      else
         return L"";
   }


   void stderr_stream_helper_write(const char *data)
   {
      DWORD RetVal;
      WriteFile(GetStdHandle(STD_ERROR_HANDLE), data, (DWORD)strlen(data), &RetVal, NULL);
   }

   void stderr_stream_helper_flush()
   {
      FlushFileBuffers(GetStdHandle(STD_ERROR_HANDLE));
   }

}