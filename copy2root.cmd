@echo off
@if /i '%echoval%' EQU 'on' echo on
setlocal

if '%1' EQU '' (
  @echo No plugin specified, make sure it's for PythonScript ver2.7
  goto :eof
)
if not exist %1 (
  @echo The plugin '%1' doesn't exist
  goto :eof
) else (
  xcopy .\%1\*.* %_path_npp%\plugins\PythonScript\scripts
)
@rem -----------------------------------------------------------------------
@rem
@rem  <|:) Wizard
@rem
@rem -----------------------------------------------------------------------