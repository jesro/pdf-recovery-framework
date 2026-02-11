@echo off
echo ================================
echo Starting PDF Recovery Web Framework...
echo ================================

docker build -t pdf-recovery-web .
docker run -p 8000:8000 pdf-recovery-web

pause