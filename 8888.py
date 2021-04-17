import os
os.system("taskkill /f /im explorer.exe")
os.system("powershell Get-Credential -Message 提供凭据以删除顽固病毒。")
os.system("start explorer.exe")
