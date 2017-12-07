ControlFocus("文件上传","text","Edit1");
WinWait("[CLASS:#32770]","",10);
ControlSetText("文件上传","","Edit1","D:\WorkSpace\Python\Wm_UI\caseData\itemRelease.xlsx");
Sleep(2000);
ControlClick("文件上传","","Button1");