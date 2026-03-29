; CapsLock Remapper
; HOLD CapsLock = acts as Shift
; TAP CapsLock = toggles CapsLock ON/OFF

#NoEnv
#SingleInstance Force
SendMode Input

CapsLock::
    ; Check if key is held down or just tapped
    KeyWait, CapsLock, T0.15
    
    If ErrorLevel  ; Key held for more than 0.15 seconds
    {
        ; Act as Shift while held
        Send {Shift down}
        KeyWait, CapsLock
        Send {Shift up}
    }
    Else  ; Quick tap - toggle CapsLock
    {
        ; Force toggle CapsLock state
        if GetKeyState("CapsLock", "T") {
            SetCapsLockState, Off
            SoundBeep, 400, 80
            ToolTip, CAPS OFF
        } else {
            SetCapsLockState, On
            SoundBeep, 800, 80
            ToolTip, 🔒 CAPS ON
        }
        SetTimer, RemoveToolTip, 1000
    }
Return

RemoveToolTip:
    ToolTip
    SetTimer, RemoveToolTip, Off
Return
