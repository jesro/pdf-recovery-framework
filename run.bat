@echo off
echo Starting PDF Recovery Framework...

docker info >nul 2>&1 || (
  start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
  timeout /t 25 >nul
)

docker build -t pdf-recovery-framework .
docker run -it --rm pdf-recovery-framework

pause