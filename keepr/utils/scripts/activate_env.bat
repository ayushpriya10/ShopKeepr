@echo off

cd %1
virtualenv env
cd env/scripts
activate
cd ../..
exit 