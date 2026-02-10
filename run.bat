@echo off
echo Starting PDF Recovery Framework...

docker info >nul 2>&1 || (
  start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
  timeout /t 25 >nul
)

docker build -t pdf-recovery .
docker run -it pdf-recovery

pause