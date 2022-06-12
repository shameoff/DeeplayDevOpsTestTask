2 задания из стажировки на DevOps-инженера в Deeplay \n

Чтобы выполнить первое задание, нужно запустить скрипт main.py \n

Чтобы выполнить второе задание, на *nix-системе, использующей systemd, нужно перенести файл DeeplayUnitInternship.service в /etc/systemd/system, 
затем выполнить следующие команды: \n
$ systemctl daemon-reload \n
$ systemctl start DeeplayUnitInternship \n
$ system enable DeeplayUnitInternship \n

P.S. на текущий момент не знаком с джавой, поэтому не совсем получилось запустить скрипт, так как в main() кидается Exception прямо с первой строчки без условий, если я правильно понял. Задумка автора ли это или загадка, которую я должен был разгадать? 
