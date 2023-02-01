# Change Log

## vexcode-0.1.0
- Initial preview release

## vexcode-0.2.0

### Features

- Added Controller VEXos update support for:
    - EXP Controller 
    - IQ 2nd Gen Controller
- Added DFU device detection and DFU VEXos recovery for:
    - EXP Brain 
    - EXP Controller 
    - IQ 2nd Gen Brain 
    - IQ 2nd Gen Controller
- Added Driver installer prompt if IQ2/EXP Controller fails recovery from DFU (Windows Only)

### Bug Fixes
- Fixed vexcom process environment  to handle spaces in absolute path. This addresses the space in username bug.   

## vexcode-0.3.0

### Features
- Added Interactive Terminal Support for V5 Controller
- Updated project import for **VEXcode Pro V5** projects **ONLY**
   - Import project will update the existing project instead of creating a new 
   project and copying the contents from the old project.   
- Added Websocket Server
   - Sends user port data to connected websocket
  

### Bug Fixes
- Vexos version compare bug.
- Fixed import project platform case. 
   - Extension could not find template projects on case sensitive file systems. 
- Updated vexicon font.  Visual Studio Code version 1.72.0 broke old icon font.