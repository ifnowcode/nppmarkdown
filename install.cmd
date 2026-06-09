@echo off
@if /i '%echoval%' EQU 'on' echo on
setlocal

if not exist %1 echo The plugin %1 doesn't exist && goto :eof

call rcopy.cmd .\%1 %_path_npp%\plugins\PythonScript\scripts\%1
@rem -----------------------------------------------------------------------
@rem
@rem  <|:) Wizard
@rem
@rem -----------------------------------------------------------------------